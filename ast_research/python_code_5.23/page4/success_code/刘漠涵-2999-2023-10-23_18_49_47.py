list1=input().split( )
list0=input().split( )
a=int(list0[0])
b=int(list0[1])
c=list1[a]
list1[a]=list1[b]
list1[b]=c
print(list1)
