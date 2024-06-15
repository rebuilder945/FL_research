a = eval(input())
n,m = map(int,input().split(','))
if n<=len(a):
    b = []
    for x in range(n):
        b.append(a[x])
    for y in range(m,len(a)):
        b.append(a[y])
    print(b)
else:
    print("error")
