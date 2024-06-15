n=int(input())
list1=[x for x in range(1,n+1)]
a=list1[0]
list1.pop(0)
list1.append(a)
print(list1)
