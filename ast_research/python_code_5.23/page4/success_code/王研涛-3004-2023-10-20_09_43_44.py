def f(x):
    c=0
    for i in range(2,x):
        if x%i==0:
            c=c+1
    if c==0:
        return 0
    elif c!=0:
        return 1
a=eval(input())
b=[]
for x in a:
    if f(x)==0:
        b.append(x)
print(b)
