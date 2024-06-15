n=eval(input())
a=[1,1]
for i in range (n):
    b=a[i]+a[i+1]
    a.append(b)
numbers=[]
for i in range(1,n+1):
    c=a[i+1]/a[i]
    numbers.append(c)
print('%.4f'%(sum(numbers)))

