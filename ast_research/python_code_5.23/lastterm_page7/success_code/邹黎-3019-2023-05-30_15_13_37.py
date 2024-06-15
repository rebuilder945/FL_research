lst=list(input().split(" "))
mingzi=lst.pop(0)
lst1=[]
for x in lst:
    x=float(x)
    lst1.append(x)
lst1.sort(reverse=True)
a=lst1[0]
b=lst1[1]
c=lst1[2]
d=sum(lst1)/len(lst1)
print("%s %.2f %.2f %.2f %.2f"%(mingzi,a,b,c,d))
