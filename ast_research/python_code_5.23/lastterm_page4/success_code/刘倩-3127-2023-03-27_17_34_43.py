n = eval(input())
a =[i for i in range(1,n+1)]
for i in range(1,len(a)):
    b = a[1:].append(a[0])
print(b)
