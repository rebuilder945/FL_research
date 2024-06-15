a = str(input())
b = eval(input())
list1 = a
list2 = b
result = [[list1,list2] for list1,list2 in zip(list1,list2)]
print(result)
