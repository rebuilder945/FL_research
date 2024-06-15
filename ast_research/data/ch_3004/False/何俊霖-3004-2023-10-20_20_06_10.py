x=eval(input())
for i in x:
    if i==1:
        x.remove(1)
    elif i==2:
        continue
    else:
        for n in range(2,i):
            if i%n==0:
                x.remove(i)
                break
            else:
                continue
print(x)
