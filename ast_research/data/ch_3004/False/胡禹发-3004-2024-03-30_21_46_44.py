a=list(eval(input()))
b=a[:]
for i in a:
    if i==1:
        1+1
    else:
        for n in range(2,i) :
            if i%n==0:
                b.remove(i)
                break
print(b)
