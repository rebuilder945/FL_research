n=eval(input())
a=1
b=2
s=0
for x in range(n):
    if x%2==0:
        s=s+b/a
        a=a+b
    else:
        s=s+a/b
        b=b+a
print('%.4f'%s)

