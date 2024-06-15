a = list(eval(input()))
n,m = eval(input())
if n<=len(a)-1:
    while m:
        a.append(a[n])
        m-=1
    print(a)
else:
    print('error')

