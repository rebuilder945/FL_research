input=eval(input())
list=[x for x in range (1,input+1)]
print(list)
a = list.pop(0)
list.insert(-1, a)
print(list)

