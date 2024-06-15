def feibo(x):
    a=[1,1]
    for i in range(x):
        b=a[-1]+a[-2]
        a.append(b)
    return a
n=eval(input())
a=feibo(n)
b=0
for i in range(n):
    d=a[i+2]/a[i+1]
    b+=d
print('%.4f'%b)


