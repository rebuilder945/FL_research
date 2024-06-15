

a=list(eval(input()))
n,m=eval(input())
b=[]
if n>=len(a):
    print('error')
else:
    for x in range(m):
        a.append(a[n])
b=a+b
print(b)
