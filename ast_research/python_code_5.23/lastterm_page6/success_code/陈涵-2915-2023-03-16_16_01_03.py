n=eval(input())
if n<=100:
    print("none")
elif n<=999:
    flag=False
    for i in range(100,n+1):
        a=i%10
        b=(i//10)%10
        c=i//100
        if a**3+b**3+c**3==i:
            print(i)
            flag=True
    if flag==False:
        print("none")
else:
    for i in range(100,1000):
        a=i%10
        b=(i//10)%10
        c=i//100
        if a**3+b**3+c**3==i:
            print(i)




