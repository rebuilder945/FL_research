def sushu(m):
    for i in range(2,m//2+1):
        if m%i==0:
            return 0
    return m
a=eval(input())
b=[]
for x in a:
    c=sushu(x)
    b.append(c)
b.remove(0)
print(b)

