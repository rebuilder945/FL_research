n=int(input())
list1=[x for x in range(1,n+1)]
print(list1)
a=list1[0]
list1.pop(0)
print(list1)
list1.append(a)
print(list1)
