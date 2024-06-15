a = eval(input())
list = [x for x in range(1,a+1)]
b = list.pop(0)
list.insert(-1,b)
print(list)


