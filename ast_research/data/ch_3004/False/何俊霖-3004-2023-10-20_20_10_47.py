x=eval(input())
for i in x:
    if i==1:
        x.remove(1)
    elif i==2:
        x=x
    else:
        for n in range(2,i):
            if i%n==0:
                if i in x:
                    x.remove(i)
            else:
                continue
print(x)
