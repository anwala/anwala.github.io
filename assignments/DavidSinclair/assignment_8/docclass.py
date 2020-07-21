#from pysqlite2 import dbapi2 as sqlite
import sqlite3 as sqlite
import re
import math

def getwords(doc):
  splitter=re.compile('\\W*')
  #print(doc)
  # Split the words by non-alpha characters
  words=[s.lower() for s in splitter.split(doc) 
          if len(s)>2 and len(s)<20]
  
  # Return the unique set of words only
  toreturn = dict([(w,1) for w in words])
  return toreturn

class classifier:
  def __init__(self,getfeatures,filename=None):
    # Counts of feature/category combinations
    self.fc={}
    # Counts of documents in each category
    self.cc={}
    self.getfeatures=getfeatures
    
  def setdb(self,dbfile):
    self.con=sqlite.connect(dbfile)    
    self.con.execute('create table if not exists fc(feature,category,count)')
    self.con.execute('create table if not exists cc(category,count)')


  def incf(self,f,cat):
    count=self.fcount(f,cat)
    if count==0:
      self.con.execute("insert into fc values ('%s','%s',1)" 
                       % (f,cat))
    else:
      self.con.execute(
        "update fc set count=%d where feature='%s' and category='%s'" 
        % (count+1,f,cat)) 
  
  def fcount(self,f,cat):
    res=self.con.execute(
      'select count from fc where feature="%s" and category="%s"'
      %(f,cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def incc(self,cat):
    count=self.catcount(cat)
    if count==0:
      self.con.execute("insert into cc values ('%s',1)" % (cat))
    else:
      self.con.execute("update cc set count=%d where category='%s'" 
                       % (count+1,cat))    

  def catcount(self,cat):
    res=self.con.execute('select count from cc where category="%s"'
                         %(cat)).fetchone()
    if res==None: return 0
    else: return float(res[0])

  def categories(self):
    cur=self.con.execute('select category from cc');
    return [d[0] for d in cur]

  def totalcount(self):
    res=self.con.execute('select sum(count) from cc').fetchone();
    if res==None: return 0
    return res[0]


  def train(self,item,cat):
    features=self.getfeatures(item)
    # Increment the count for every feature with this category
    for f in features:
      self.incf(f,cat)

    # Increment the count for this category
    self.incc(cat)
    self.con.commit()

  def fprob(self,f,cat):
    if self.catcount(cat)==0: return 0

    # The total number of times this feature appeared in this 
    # category divided by the total number of items in this category
    return self.fcount(f,cat)/self.catcount(cat)

  def weightedprob(self,f,cat,prf,weight=1.0,ap=0.5):
    # Calculate current probability
    basicprob=prf(f,cat)

    # Count the number of times this feature has appeared in
    # all categories
    totals=sum([self.fcount(f,c) for c in self.categories()])

    # Calculate the weighted average
    bp=((weight*ap)+(totals*basicprob))/(weight+totals)
    return bp




class naivebayes(classifier):
  
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.thresholds={}
  
  def docprob(self,item,cat):
    features=self.getfeatures(item)   

    # Multiply the probabilities of all the features together
    p=1
    for f in features: p*=self.weightedprob(f,cat,self.fprob)
    return p

  def prob(self,item,cat):
    catprob=self.catcount(cat)/self.totalcount()
    docprob=self.docprob(item,cat)
    return docprob*catprob
  
  def setthreshold(self,cat,t):
    self.thresholds[cat]=t
    
  def getthreshold(self,cat):
    if cat not in self.thresholds: return 1.0
    return self.thresholds[cat]
  
  def classify(self,item,default=None):
    probs={}
    # Find the category with the highest probability
    max=0.0
    for cat in self.categories():
      probs[cat]=self.prob(item,cat)
#      print('Classies',cat)
#      print('item',item)
      if probs[cat]>max: 
        max=probs[cat]
        best=cat

    # Make sure the probability exceeds threshold*next best
    for cat in probs:
      if cat==best: continue
      if probs[cat]*self.getthreshold(best)>probs[best]: return default
    return best

class fisherclassifier(classifier):
  def cprob(self,f,cat):
    # The frequency of this feature in this category    
    clf=self.fprob(f,cat)
    if clf==0: return 0

    # The frequency of this feature in all the categories
    freqsum=sum([self.fprob(f,c) for c in self.categories()])

    # The probability is the frequency in this category divided by
    # the overall frequency
    p=clf/(freqsum)
    
    return p
  def fisherprob(self,item,cat):
    # Multiply all the probabilities together
    p=1
    features=self.getfeatures(item)
    for f in features:
      p*=(self.weightedprob(f,cat,self.cprob))

    # Take the natural log and multiply by -2
    fscore=-2*math.log(p)

    # Use the inverse chi2 function to get a probability
    return self.invchi2(fscore,len(features)*2)
  def invchi2(self,chi, df):
    m = chi / 2.0
    sum = term = math.exp(-m)
    for i in range(1, df//2):
        term *= m / i
        sum += term
    return min(sum, 1.0)
  def __init__(self,getfeatures):
    classifier.__init__(self,getfeatures)
    self.minimums={}

  def setminimum(self,cat,min):
    self.minimums[cat]=min
  
  def getminimum(self,cat):
    if cat not in self.minimums: return 0
    return self.minimums[cat]
  def classify(self,item,default=None):
    # Loop through looking for the best result
    best=default
    max=0.0
    for c in self.categories():
      p=self.fisherprob(item,c)
      # Make sure it exceeds its minimum
      if p>self.getminimum(c) and p>max:
        best=c
        max=p
    return best

def spamTrain(cl):
  cl.train('2018 73679 above accounting action active address after and appear april askdfas asked aspx authenticated automatically available bar browser category click clients com contact contained copy corpweb1 custmain cybersecurity date dcps defense delivered dfas disabled document dsincl1999 due earnings edt electronic email enter entire feature field finance find flps folders follow for frequently from have help highlighted https hyperlinks increased into leave les like link links list location longer mail mailbox may messages mid mil mypay need not open option organized paste personalized picking please press print protocols question questions replies reply review sent service site smartdocs some statement steps subject submit taken that the there these this unmonitored visit web wednesday well will window would yahoo you your', 'not spam')
  cl.train('6th 10th 683 757 2018 3192 about academics activist activities aid all amazon amold and announ announcement announcements any appropriate apr april are athletic athletics award bad below blood cafe calling card career chapman click com contact convenience credit david day defense department details dominion drive dsinc002 edu effective elaine email employee equipment explore f6a80 fair fee feminist financial fletcher for free gift global google graduate have hidden honor https ilr increase individual international its itshelp join juniors link listed mail may message messages mondays money month movie national natural negotiation night not notices odu old online only park participate photo planetarium please poetry positions post posted questions quoted recreation regarding reply respond room salary scholarship school self seniors shoot shows signature sinclair smart social sophomores spring start steve student students study subject summer system text thailand the this thursdays today tourism travel tuesday university view volunteer web wed wednesday who women workshop yetiv you', 'not spam')
  cl.train('6th 12pm 19th 683 757 2018 3192 about academics activist activities aid ally amold and announcement announcements any apple appropriate apr april are award awards bad beach below big biological blood blue bookstore bound cafe calendar camp card challenge chapman chemistry choir click closures com concert contact convenience coussens credit daily dance david day defense details development dominion drive dsinc002 edu effective elaine email employee ensemble events exam f6a80 faculty fair fee feminist financial fletcher floor flute following for free gcp global good google graduate hace have honor how https ilr increase individual innovation its jam juniors kentucky learned link listed mail maintenance mark may message monday mondays month morning movie nanny nathan national nato natural negotiation news next night nomination not notices now odu oklahoma old one only open opens panel photo pizza planetarium please poetry post posted program promotions questions rangnekar read reception regarding registration reply respond road safe safety salary sale sales scholar scholarship sciences seeking self seminar seniors series share shoot shows sinclair site smart social sophomores space spring staff start steve student subject summer system talent thailand the this thursdays today tomorrow tonight training triathlon udt univ university upward view village virginia vivek walking walkthrough web wed wednesday who wind women workshop yetiv you your','not spam')
  cl.train('9am 2018 3316 23529 abstract advisor all amold and application applications apr april are ariel ask associate attend attendance based baseline basis been big building can charging cloud colloquium com committee common computer computing conference connection could counts data datacenter david decker defens defense department developed director discussion dominion dormant dsinc002 edge edu electric electrical enough environment exists f6a80 faculty for form further google grad graduate great handle has have hidden http https infrastructure interconnected investigate investigation invited its larger lloyd long mail many member members messages michele mobile mweigle networks norfolk not odu olariu old parked place processing professor program provide put question quoted receive requirement resources return room sci science sensor services simply sinclair sturtevant supporting text that the their then there these thesis they this towards tue university untapped use utilization utilize vehicle vehicles vehicular waiting weigle were when whether will with www zeil','not spam')
  cl.train('43rd 683 757 888 2018 3097 3435 23529 advanced alumni amold and apr april association attire barry big blue brought business casual center click com complimentary connect constant convocation cordially david degree dominion dsinc002 edu email f6a80 for from garage google graduate group guest here https invited invites kornblau limited list luncheon mail mailing may message norfolk odu odualumni old one org page parking removed reply room rsvp sinclair space sponsored street ted the this thursday time tue university update view web when where wish with www you','not spam')
  cl.train('2018 any apr are areas avaya calling capability com concerns conference contact david dominion dsinc002 each edu effective f6a80 feel for forward free from going google grad graduate group have hidden https immediately indivi individual just lab left mail messages mon odu old one per phone phones place please questions quoted removal removing research root sci sinclair students systems text the there university will work','not spam')
  cl.train('683 757 2018 3300 4700 7796 23529 achieve addressed agent ali allow amold and any apr are ariel assistant asturtev attachment ave believe bldg can colloquium com communication computational computer conceive confidential confidentiality contain contained copied copies copy david delete department dominion dsinc002 edu either elkhorn email engineering entity error event f6a80 faculty federal for found friday google grad graduate have heart https immediately individual information intended know lost mail main manner may message mind mon muhammad nature norfolk not notebook notice notify odu office old original other our permanently person phone phyl phyllis please privacy privileged program programs purple read received recipient regulations response sci science sciences sender should sinclair state stop sturtevant subject suite tell thank that the their them then this university use utilized website which who whom within woods www you','not spam')
  cl.train('2nd 29k 2018 add amold and anything apr attempt com computer david department diamon docx dominion dsinc002 edu engineer f6a80 first fri friday from get google here https know layer3 let mail mar march messages mon need networking odu old over paper please projects reading science second sent sinclair sometime subject systems thank that the this today university wiggins will working you','not spam')
  cl.train('1st 10am 11am 45am 2017 2018 23529 able academic and apr are ariel arrive asked associate attend auditorium bpqnn5wko6veftyx1 building can com computer david department director dominion dsinc002 edu email event f6a80 families floor for forms friends goo google grad graduate graduates graduation held help http https mail may message michele mon mweigle need norfolk not odu old phd planning please professor program promptly reception rsvp science sinclair start sturtevant the university weigle will with www year you your','not spam')
  cl.train('1st 2018 ability abstract activefaculty adding alias allen alter amold and announcements anyone apr april archives are asking assistant associate attendance attention attract audio auditorium authenticate automatically available based become beth biochemistry biology bliss broader building chair chairs charles chemistry christophe civey colloq colloquium collquium com computer content context convincing cooper credit csukenik cultural curt cusp cvern002 david davie dept digital dimension director discourse disinformation dnguyen dodge dominion donuts dsinc002 edu else email esanc001 evidence existing f6a80 faculty fake floor for forward fri friday gail gdodge gmail google gov grad graduate group harris harvey hgarcia hideaki historical hkaneko hotmail html http https hwu hynes image inbox included increasingly integrity interested ivey james jbliss jcooper john johnson jon jrobi075 kaneko kdavi068 kristen larc laundering libraries liu mail martin math media message michael mitre mmart081 moment mon msosonkina nasa needing nelson new news not obfuscate odu oeas office old one online opportunities order org our photoshop physics please political present primary probably problem produce professor program provenance psychology r_armijos rdc receive receiving record requirements resources review rharvey robison roger root rude schedule sci science seek send shampooair short should sinclair social solution soon source sources spread staff steven students sukenik synthetic syskids systems szeil talk text the them then these they this those threats time trustworthy university untrustworthy vector vernon video viewing wayne weaponized web weigle who whynes will wishing working would www yahoo z1liu zeil zhanping','not spam')
  cl.train('2018 73514 ages amprint and april asap click com contact date dateworld4fck dining drug dsincl1999 edt emails enjoy female folders for free from getting greta567 happy here hook http https looking lovely mail make man meet messages monday movies music out please print rzyve stop subject sweet swingers there who will window www yahoo', 'spam')
  cl.train('2018 73500 and april area available chavez click com comfort could date david dsincl1999 easy edt few folders from guaranteed have here home https interested mail make malachi malachichavez0955 messages mins monday money need note now only part pinehurstabbey print proven see show soon spots subject the this time unsubscribe way window working worth would yahoo you your', 'spam')
  cl.train('02142 2017 2018 9998 73410 425768 affordable american and april are box cambridge com compare could covered date david dsincl1999 edt email family find folders for from here https insurance life mail marketing message messages onthewaytocancun plan print protect save subject sunday this today tomorrow unsubscribe waiting what window with yahoo you your yourself', 'spam')
  cl.train('250 2018 10620 73430 92131 administration affiliated already amprint and any applied april are been boost bundles codes coffee com compatible cup cure date day diagnose diego discount disease drug dsincl1999 due edt email emails energy essential evaluated folders food from full future giving great green have here https icomefromcancun inc instant intended into keurig mail marketing message messages mountain not off owned packs prefer prevent print product promo receive registered right roasters san serving start statements subject subsidiary sunday tastes the these this trademarks treat treena unsubscribe valid vitacup vitamins wholly window with yahoo you your', 'spam')
  cl.train('07675 502 2018 73407 alright amber amprint april bloomberg blunt built bunny buzz click colbert com creepy date detailspark diy dress dsincl1999 easter edt eletter emily finds folders fox from here https idea introduction late lele like little mail makeover mary messages must news nhl nice old onlinevideo plaza pons poppins print prom quite request save scholl send show sports state stephen subject sunday tank tappan the unsubscribe wheelchair window with yahoo you your', 'spam')
  cl.train('16th 2017 2018 10004 73406 ability able accounting adverse advertisement advice all amount amprint and approximate april are assume assurance attorney available away bankruptcy based before broadway calls can circumstances claims clients com company complete consequences consult consumer contact content copyright credit creditors date debt debts depending discuss dsincl1999 edt eligible enrolled enrollment estimate estimates fees floor folders for free from funds get guarantee how https impact including information legal llc local lowered mail make materials may messages monitored monthly months more national new not note obligation our over panoramicdirection payments percentage period please potential print prior professional program provide purposes quality quickly rating read ready realize reasons recommend recorded relief repair reserved results rights save savings see services settled settlement specific state states stay subject sufficient sunday tax that the their this time training understand unsubscribe upfront usa various vary which who will window with within yahoo york you your', 'spam')
  cl.train('02116 175 477 866 1118 2017 2018 73405 accident advertising affiliated affiliates all amprint and annual apply april are assistance associated availability available average based because behalf below benefits berkeley boston brand call car change claims columbia com commercial company comparison conditions contains content could countrywide coverage customers database date depreciated district does dsincl1999 due easy edt effective eligibility email emails enjoy entire expressed fast first folders for forgiveness from full further get getting guarantee guaranteed have help here hour https impacts increase information insurance interest interested its liberty licensed like list mail marketers marketing may message messages mid month mutual nature need new not offered one optional party please policy prefer premium premiums previously print prior products promotional provided provider quote rate ready receive receiving refer regarding reimbursed replacement reported risk rules saving savings sent services site sites some state states street subject sunday survey switched term terms that the them there these they third this through underwriting underwritten unsubscribe usa value varies was when whenever who window wish with won would yahoo year you your zipperpopcorn', 'spam')
  cl.train('02140 139 1373v1 1770 2018 4477 73404 97076 about achievement advertisement affect america amprint and apply april are associate ave bank based beaverton box cambridge can card cardconnection click com company complete credit date designed determine dsincl1999 easy edt email emails folders for form from fundedco genesis gold here https issued itself journey less like mail managing marketing massachusetts mastercard messages mid milestone not now offer one oregon our perfect please potential pre prequalified print profile qualification qualify qualifying quick receiving represents score sent serviced services special stop subject successfully sunday than the this those tool toothears trust unsubscribe was will window wish with would write yahoo you your', 'spam')
  cl.train('185 2017 2018 5000 73401 94107 advertisement amprint and april berry click code com content credits date download dsincl1999 edt email5 folders francisco from get here https inc interestdecisive lyft mail messages minutes please print repeat request ride san subject suite sunday this unsubscribe use way window with write yahoo you your', 'spam')
  cl.train('400 1455 2018 73400 94103 affiliate april are based com company content date drive dsincl1999 edt email emails enjoyed expressed folders francisco from hope https inc interest invited link longer mail market marketing messages partner pensubstance previously print products receive receiving san services should subject suite sunday technologies this through uber unsubscribe visit window wish with yahoo you your', 'spam')

