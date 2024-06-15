n=eval(input())
for i in range(1,n+1):
    c=i%100
    a=i//100
    b=i//10//10
    if a**3+b**3+c**3==a*100+b*10+c:
        print(i)
    else:
        print("none")

