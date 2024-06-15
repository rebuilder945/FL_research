lst1=input().split()
n,m=input().split()
a=int(n)
b=int(m)
lst2=lst1.copy()
lst2[a]=lst1[b]
lst2[b]=lst1[a]
print(lst2)




