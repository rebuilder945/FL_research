lst=eval(input())
n=lst.count(0)
lans=[0]*n
lst2=[]
for x in lst:
    if x==0:
        continue
    else:
        lst2.append(x)
lst3=lst2+lans
print(lst3)

