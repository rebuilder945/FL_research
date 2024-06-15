a=eval(input())
list1=list(range(1,a))
list1.append(list1[0])
del list1[0]
print(list1)

