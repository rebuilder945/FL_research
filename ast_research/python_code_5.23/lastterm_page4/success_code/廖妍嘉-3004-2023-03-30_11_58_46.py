def f(x):
    if x<=1:
        return False
    if x==2:
        return True
    for i in range(2,x):
        if x%i==0:
            return False
        else:
            return True
ls=eval(input())
ls2=[]
for x in ls:
    if f(x):
        ls2.append(x)
print(ls2)
