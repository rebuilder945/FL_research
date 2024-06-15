a=eval(input())
z=[]
def ss(n):
    for i in range(2,n):
        t=n%i
        if t==0:
            break
    else:
        return True
for i in a:
    t=ss(i)
    if t and i!=0 and i!=1:
        z.append(i)
print(z)
