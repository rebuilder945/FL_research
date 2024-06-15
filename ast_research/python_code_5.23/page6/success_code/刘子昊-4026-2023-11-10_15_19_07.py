n=eval(input())
a,b=1,2
s=0
for i in range(n):
    s+=b/a
    b=a+b
    a=b-a
print('%.4f'%s)


