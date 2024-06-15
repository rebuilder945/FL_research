a=eval(input())
if a>=1000:
    a=1000
    for i in range(100,a):
        n=a//100
        m=a%100//10
        l=a%10
        if i==n**3+m**3+l**3:
            print(i)
elif a>100:
    for i in range(100,a+1):
        n=a//100
        m=a%100//10
        l=a%10
        if i==n**3+m**3+l**3:
            print(i)
else:
    print("none")
    

    

        







