def f(x):
    if x<=1:
        return False
    if x==2:
        return True
    for i in range(2,x):
            if x%i==0:
                return False
            return True
ls=eval(input())
ls2=[]
for n in ls:
    if f(n):
        ls2.append(n)
print(ls2)

