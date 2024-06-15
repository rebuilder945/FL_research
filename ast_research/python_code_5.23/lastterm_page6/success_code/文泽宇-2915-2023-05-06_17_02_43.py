n=eval(input())
if n<=100:
    print("none")
else:
    a=n//100
    b=n//10 - a*10
    c=n-a*100-b*10
    if a**3 + b**3 + c**3 == n:
        print(n)
