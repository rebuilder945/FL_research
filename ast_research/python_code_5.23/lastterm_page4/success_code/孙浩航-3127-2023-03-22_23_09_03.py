a=int(input())
b=a+1
list1=list(range(b))

aa=list1[1]
list1.remove(0)
list1.remove(1)
list1.append(aa)
print(list1)

