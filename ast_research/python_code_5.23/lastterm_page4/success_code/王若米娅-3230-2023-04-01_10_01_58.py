lst=eval(input())
lst.sort()
lst2=[]
for i in range(len(lst)):
    a=lst[i]*10**i
    lst2.append(a)
c=sum(lst2)
print(c)
