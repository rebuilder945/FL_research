'''a=eval(input())
b=[]
for x in a:
    if x >=2:
        for j in range(1,x):
            if x%j==0:
                b.append(x)
        print(b)
    else:
        c=1
        print(c)'''
a=eval(input())
n,m=map(int,input().split(','))
if n>m or n>len(a):
    print('error')
else:
    for x in range(n,m):
        del a[x]
print(a)

