names=input().split(",")
scores=input().split(",")
ls=[]
for i in range(1,len(names)+1):
    ls.append([names[i],scores[i]])
print(ls)
