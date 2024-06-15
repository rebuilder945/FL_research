n=eval(input())
flag=0
if n<100:
    flag=0
else:
    for i in range(100,n+1):
        a=i//100
        b=(i//10)%10
        c=i%10
        if i==a**3+b**3+c**3:
            print(i)
            flag=1
        if i==999:
            break
if flag==0:
    print("none")

