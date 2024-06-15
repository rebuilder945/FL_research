n=eval(input())
for i in range(100,n):
    a=i//100
    b=(i-a*100)//10
    c=i%10
    if a**3+b**3+c**3==i:
        print(i)
