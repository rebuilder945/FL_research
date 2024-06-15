i=int(input())
list1=list(range(1,i+1,1))
a=list1[0]
list1.remove(a)
list1.append(a)
print(list1)
