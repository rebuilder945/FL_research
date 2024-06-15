a=list(eval(input()))
b=a[:]
for i in a:
    if i==1:
        b.remove(1)
    elif i==0:
        b.remove(0)
    else:
        for n in range(2,i) :
            if i%n==0:
                b.remove(i)
                break
print(b)
