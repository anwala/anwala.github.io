#!/bin/bash

counter=1
while [ $counter -le 150 ]
do
  url="$(curl -L -s -o /dev/null -w %{url_effective} 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117')"
  echo $url >> blogurl.txt
  ((counter++))
  echo counter
done
echo All done
#
#curl -Ls -o /dev/null -w %{url_effective} 
#content = "$(curl -I -L 'http://www.blogger.com/next-blog?navBar=true&blogID=3471633091411211117')"
#echo "$content" #>> blogurl.txt

