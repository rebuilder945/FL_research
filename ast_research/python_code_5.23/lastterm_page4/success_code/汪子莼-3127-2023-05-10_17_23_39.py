n=eval(input())
a=[x for x in range(1,n+1)]
for i in range(1):
    b=a.pop(0)
    a.append(b)
print(a)

