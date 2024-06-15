n=eval(input())
lst=[x for x in range(1,n+1)]
a=lst[0]
lst1=[]
for x in range(len(lst)-1):
    lst1.append(lst[x+1])
lst1.append(a)
print(a)


