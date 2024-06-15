def a(n):
    if n<=1:
        return False
    for i in range(2,n):
        if n%i==0:
            return False
    return True
b=eval(input())
c=[]
for n in b:
    if a(n):
        c.append(n)
print(c)
