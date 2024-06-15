a=list(map(int,input().split(',')))
m,n=eval(input())
if n<len(a)-1:
    if m>=0:
        for i in range(n):
            a.append(a[m])
        print(a)
    if m<0:
        for i in range(n):
            a.append(a[m])
            m-=1
        print(a)

else:
    print("error")
