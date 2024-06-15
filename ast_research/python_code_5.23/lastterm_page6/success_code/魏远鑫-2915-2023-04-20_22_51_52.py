n=eval(input())
for i in range(n):
    a=i//100
    b=i//10-10*a
    c=i%10
    if a**3+b**3+c**3==i and 1 <= a**3+b**3+c**3<1000 :
        print(i)


