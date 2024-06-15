a=eval(input())
for n in a:
    for i in range(2,n):
        if n%i==0:
            a.remove(n)
        else:
            pass
print(a)
