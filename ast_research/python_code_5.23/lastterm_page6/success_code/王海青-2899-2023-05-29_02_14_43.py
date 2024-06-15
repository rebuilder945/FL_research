list1=input().split()
m,n=input().split()
a=int(n)
b=int(m)
q=list1[a]
list1[a]=list1[b]
list1[b]=q
print(list1)
