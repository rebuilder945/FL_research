list1=input().split()
m,n=input().split()
a=int(m)
b=int(n)
q=list1[a]
list1[a]=list1[b]
list1[b]=q
print(list1)




