a=list(eval(input()))
b=a.copy()
for i in a:
    for n in range(1,a[i]) :
        if a[i]%n==0:
            b.remove(a[i])
print(b)
