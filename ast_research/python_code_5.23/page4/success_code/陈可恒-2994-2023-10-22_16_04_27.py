a = list(eval(input()))
b = a.copy()
n,m = eval(input())
if n<=len(a)-1:
    while m:
        b.append(a[n])
        m-=1
    print(b)
else:
    print('error')

