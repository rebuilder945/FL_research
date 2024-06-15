n=eval(input())
a=[]
for i in range(1,n+1):
    a.append(i)
    one=a[0]
    for x in range(len(a)-1):
        a[x]=a[x+1]
        a[x+1]=one
        print(a)

