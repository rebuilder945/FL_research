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
if 0 in b:
    b.remove(0)
if 1 in b:
    b.remove(1)
print(b)

