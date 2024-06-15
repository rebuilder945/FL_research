n=eval(input())
lst=[]
lst2=[]
for i in range(1,n+1):
    lst.append(i)
for m in lst[1:]:
    lst2.append(m)
x=lst[0]
lst2.append(x)
print(lst2)


