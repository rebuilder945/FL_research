

a=list(eval(input()))
n,m=eval(input())
b=[]
if n<=len(a):
    for x in range(m):
        a.append(a[n])
else:
    print('error')
b=a+b
print(b)
