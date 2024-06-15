names=input().split(",")
results=map(int,(input().split(",")))
zipped=zip(names,results)
lst=list(zipped)
lst2=[]
for x in lst:
    re=list(x)
    lst2.append(re)
lst2.sort(key=lambda x:x[1])
print(lst2)
