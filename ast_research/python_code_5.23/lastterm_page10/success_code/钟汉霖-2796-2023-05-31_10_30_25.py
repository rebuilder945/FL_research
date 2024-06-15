def f(x):
    y='1234567890'
    for i in x:
        if not i in y:
            return False
    return True
a=input()
b=''
n=len(a)
for start in range(n):
    for end in range(start,n+1):
        if f(a[start:end]) and (end-start)>=len(b):
            b=a[start:end]
if b=='':
    print('No digits')
else:
    print(b)
