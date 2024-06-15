a=list(eval(input()))
b=a.copy()
n,m=eval(input())
if n <len(a):
    for i in range(m):
        a.append(b[n])
    print(a)
else:
    print('error')
