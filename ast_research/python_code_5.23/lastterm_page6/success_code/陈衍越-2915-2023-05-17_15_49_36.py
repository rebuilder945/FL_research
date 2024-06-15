n=int(input())
if n<100:
    print('none')
else:
    t=min(n+1,999)
    flag=0
    for i in range(100,t):
        a=i//100
        c=i%10
        b=i//10%10
        if i==a**3+b**3+c**3:
            flag=1
            print(i)
    if flag==0:
        print('none')
