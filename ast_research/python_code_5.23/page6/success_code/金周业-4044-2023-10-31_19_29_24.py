n=eval(input())
x=0
y=0
if n <1000:
    for i in range(100,n+1):
        a=i//100
        b=i//10%10
        c=i%10
        if i == a**3+b**3+c**3:
            print(i)
            y=y+1
else:
    for i in range(100,1000):
        a=i//100
        b=i//10%10
        c=i%10
        if i == a**3+b**3+c**3:
            print(i)
            y=y+1
if y==0:
    print("none")





