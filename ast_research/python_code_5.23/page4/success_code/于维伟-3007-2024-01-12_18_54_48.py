a=input().split(',')
n,m=map(int,eval(input()))
if n>len(a):
    print('error')
elif n>m:
    print('error')
else:
    c=[]
    for x in range(n):
        c.append(a[x])
    for i in range(m,len(a)):
        c.append(a[i])
    print(c)
