a = list(eval(input()))
n,m = eval(input())
b = a[n]
if n<=len(a)-1:
    for i in range(m):
         a.append(b)
    print(a)
else:print('error')
