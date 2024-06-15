a=eval(input())
b=list(range(1,a+1))
for i in b:
    if i!=a:
        b[i-1]=b[i]
    else:
        b[i-1]=1
print(b)

