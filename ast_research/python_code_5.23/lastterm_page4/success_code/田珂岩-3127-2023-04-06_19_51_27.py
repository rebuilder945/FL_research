n = int(input())
a = [x for x in range(1,n+1)]
b = a.pop()
a.insert(0,b)
print(a)
