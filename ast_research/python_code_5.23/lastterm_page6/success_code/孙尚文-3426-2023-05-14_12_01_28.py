def hanshu(x):
    if x<20:
        print(6*x**2+1)
    if 20<=x<40:
        print((3*x-60)**0.5)
    if x>=40:
        print(100/(x+1))
x=eval(input())
hanshu(x)
