a=input().split(",")
b=input().split(",")
zipped=zip(a,b)
lst=list(zipped)
lst2=[]
for x in lst:
    re=list(x)
    lst2.append(re)
print(lst2)
