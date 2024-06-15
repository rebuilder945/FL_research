n=eval(input())
lst1=range(1,n+1)
lst2=[]
m=lst1[0]
for i in range(len(lst1)-1):
    lst2.append(lst1[i+1])
lst2.append(m)
print(lst2)
