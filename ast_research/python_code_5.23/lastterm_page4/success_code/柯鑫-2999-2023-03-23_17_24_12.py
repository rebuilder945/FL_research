list1=list(input().split())
a,b=map(int,input().split())
c=list1[a]
d=list1[b]
list1[b]=c
list1[a]=d
print(list1)
