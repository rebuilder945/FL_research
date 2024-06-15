def m(n):
    flag=True
    for i in range(100,n+1):
        sum=0
        for a in str(i):
            sum=sum+(int(a)**3)
        if sum==i:
            print(sum)
            flag=False
    if flag:
        print('None')
z=eval(input())
m(z)

