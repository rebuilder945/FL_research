a = eval(input())
m,n = eval(input())
c = []
if m >= len(a):
    print('error')
else:
    for i in range(n):
        c.append(a[m])
        print(a+c)

