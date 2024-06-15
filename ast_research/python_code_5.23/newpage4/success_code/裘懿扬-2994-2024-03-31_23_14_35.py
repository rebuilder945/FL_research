a=input().split(",")
n,m=eval(input())
c=[]
for x in a:
    c.append(int(x))
b=c.copy()    
if n<=len(a):
    for i in range(0,m):
        b.append(c[n])
    print(b)
else :
    print('error')


