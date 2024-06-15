a=list(eval(input()))
b=a[::]
n,m=eval(input())
if n>len(a):
    print('error')
else:
    for i in range(m):
        b.append(a[n])
    print(b)
