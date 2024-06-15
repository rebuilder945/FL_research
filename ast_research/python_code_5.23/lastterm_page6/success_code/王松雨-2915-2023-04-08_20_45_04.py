n=eval(input())
if 100<n<1000:
    for i in range(100,n+1):
        a=i%10
        b=i//10%10
        c=i//100
        if i==a**3+b**3+c**3:
            print(i)
elif n>1000:
    for i in range(100,1000):
        a=i%10
        b=i//10%10
        c=i//100
        if i==a**3+b**3+c**3:
            print(i)

else:
    print("none")

