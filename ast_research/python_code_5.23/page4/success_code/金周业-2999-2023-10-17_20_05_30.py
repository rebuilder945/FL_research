list1=input().split()
list2=input().split()
a=int(list2[0])
b=int(list2[1])
list1[a],list1[b]=list1[b],list1[a]
print(list1)

