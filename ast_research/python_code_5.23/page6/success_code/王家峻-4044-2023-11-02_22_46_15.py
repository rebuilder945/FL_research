n=eval(input())
for i in range(n):
    a=i%10
    b=i//10%10
    c=n//100
    if a**3+b**3+c**3==i:
        print(i)
    else:
        print(None)
