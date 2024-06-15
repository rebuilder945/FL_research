n=eval(input())
a,b=2,1
sum=0
for i in range(n):
    c=a/b
    sum+=c
    a,b=a+b,a
print('%.4f'%(sum))
