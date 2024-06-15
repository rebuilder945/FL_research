names=input().split(",")
scores=input().split(",")
finallist=[]
for i in range(len(names)):
    newlist=[]
    newlist.append(names[i])
    newlist.append(eval(scores[i]))
    finallist.append(newlist)
finallist.sort(key=lambda x:x[1])
print(finallist)
