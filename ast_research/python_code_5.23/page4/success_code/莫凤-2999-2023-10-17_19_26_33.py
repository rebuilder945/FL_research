list1=input().split()
a,b=list(map(int,input().split()))
list1[a],list1[b]=list1[b],list1[a]
print(list1)
