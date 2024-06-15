a = list(eval(input()))
n,m = eval(input())
if n<=len(a)-1:
    b = a[n]
    for i in range(m):
         a.append(b)
    print(a)
else:print('error')



