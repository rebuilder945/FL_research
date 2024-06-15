a = eval(input())
b = list(range(1,a+1))
b.append(1)
del b[0]
print(b)
