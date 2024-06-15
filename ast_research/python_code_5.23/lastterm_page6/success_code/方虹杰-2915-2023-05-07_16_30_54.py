a=int(input())
if a<=100:
    print("none")
elif a>=1000:
    for i in range(100,1000):
        x=i//100
        y=i//10%10
        z=i%10
        if x**3+y**3+z**3==i:
            print(i)
else:
    for i in range(100,a+1):
        x=i//100
        y=i//10%10
        z=i%10
        if x**3+y**3+z**3==i:
            print(i)


