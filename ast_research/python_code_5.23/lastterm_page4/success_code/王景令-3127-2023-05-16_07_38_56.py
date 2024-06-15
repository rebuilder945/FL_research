n = eval(input())
b = [x+1 for x in range(n)]
b.append(b.pop(0))
print(b)
