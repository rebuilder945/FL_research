a = list(eval(input()))
n,m = eval(input())
if n<=len(a)-1:
    while m:
        a.append(a[n])
    print(a)
else:
    print('error')

