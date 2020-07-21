import matplotlib.pyplot as plt

#with open('histograph.datai') as f:

finalGrades = [12,2,7,1,1,18,2,27,13,4,1,2,10]
plt.hist(finalGrades, bins=8)

plt.title("Historgram Plot of Memo")
plt.xlabel("Number of Memo")
plt.ylabel("Number of")
plt.show()

