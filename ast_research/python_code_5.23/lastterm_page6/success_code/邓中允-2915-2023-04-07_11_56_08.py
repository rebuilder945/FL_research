n=eval(input())
for i in range(100,n+1):
    a=i%10
    b=(i//10)%10
    c=i//100
    if (a**3+b**3+c**3)==(a*100+b*10+c):
        d=c*100+b*10+a
        print(d)
    else:
        print("none")
