def f(x):
    if x<20:
        m=6*x**2+1
    elif x>=20 and x<40:
        sum=3*x-60
        m=pow(sum,0.5)
    elif x>=40:
        m=100/(x+1)
    print("%.2f"%m)


a=eval(input())
n=f(a)    
