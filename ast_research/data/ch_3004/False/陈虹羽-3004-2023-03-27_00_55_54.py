a=eval(input())
b=a.copy()
for i in b:
    if i==0 or i==1:
        b.remove(i)
    elif i==2:
        pass
    else:
        for x in range(2,i):
            if i%x==0:
                b.remove(i)
                break
print(b)
