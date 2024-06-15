a = eval(input())
b = [i for i in range(1,a+1)]

c = b[0]
del b[0]
b.append(c)
print(b)
