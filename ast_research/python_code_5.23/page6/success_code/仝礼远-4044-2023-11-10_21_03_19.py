def m(n):
    flag=True
    sum=0
    for i in range(n+1):
        for a in str(i):
            sum=sum+int(a)**3
        if sum == i:
            print(i)
            flag=False
    if flag:
        print('None')
m(eval(input()))

