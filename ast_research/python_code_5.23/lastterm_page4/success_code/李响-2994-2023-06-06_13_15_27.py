a = eval(input())
m,n = eval(input())
c = []
if m >= len(a):
    print('error')
else:
    c.append(a[m]*n)
    print(a+c)

