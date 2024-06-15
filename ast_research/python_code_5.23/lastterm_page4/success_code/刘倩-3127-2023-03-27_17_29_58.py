n = eval(input())
a =[i for i in range(1,n+1)]
for i in range(1,len(a)):
    a[1:].extend(a[1])
print(a)
