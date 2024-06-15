#第一种：
a = eval(input())
n,m = map(int,input().split(','))
if n <= len(a):    
    b = []
    for x in range(n):
        b.append(a[x])
    for i in range(m,len(a)):
        b.append(a[i])
    print(b)
else:
    print('error')

