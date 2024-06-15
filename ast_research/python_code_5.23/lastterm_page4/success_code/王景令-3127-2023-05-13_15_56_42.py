n = eval(input())
b = [x+1 for x in range(n)]

c = [b[1:],b.pop(0)]
print(b)
