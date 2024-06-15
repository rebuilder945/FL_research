n=eval(input())
lst=[]
if n>999:
    n=1000
for x in range(100,n+1):
    a=str(x)
    b=int(a[0])**3+int(a[1])**3+int(a[2])**3
    if b==x:
        print(b)
        lst.append(b)
if len(lst)==0:
    print('none')


