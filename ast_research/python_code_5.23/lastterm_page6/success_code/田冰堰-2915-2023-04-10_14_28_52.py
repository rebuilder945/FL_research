a=eval(input())
if a<153:
    print("none")
else:
    x=a%10
    y=a//10%10
    z=a//100
    for i in range(x):
        for j in range(y):
            for k in range(z):
                if a==x**3+y**3+z**3:
                    print(a)
