n=eval(input())
if n<101:
    print("none")
else:
    for i in range(100,n+1):
        a=i//100
        A=a**3
        b=(i-a*100)//10
        B=b**3
        c=i%10
        C=c**3
        if A+B+C==i:
            print(i)

