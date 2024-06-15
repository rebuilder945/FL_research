a=eval(input())
list1=list(range(1,a+1))
list1.append(list1[0])
del list1[0]
print(list1)

