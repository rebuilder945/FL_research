a=eval(input())
a=list(a)
n,m=eval(input())
if n>len(a):
    print('error')
else:
    for x in range(m):
        a.append(a[n])
print(a)
