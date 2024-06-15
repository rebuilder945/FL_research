n = eval(input())
a =[i for i in range(1,n+1)]
b = a[1:].extend([a[0]])
print(b)
