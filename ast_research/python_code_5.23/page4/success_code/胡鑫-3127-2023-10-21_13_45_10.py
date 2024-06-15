a = eval(input())
i = 1
list = []
for i in range (1,a+1):
    if i <= a:
        list.append(i)
        i += 1
    else:
        pass
list.remove(1)
list.append(eval("1"))
print(list)

