a=input().split(',')
n,m=eval(input())
c=[]
if n>len(a):
    print('error')
elif n>=m:
    print('error')
else:
    for x in range(n):
        c.append(a[x])
    for i in range(m,len(a)):
        c.append(a[i])
print(c)
