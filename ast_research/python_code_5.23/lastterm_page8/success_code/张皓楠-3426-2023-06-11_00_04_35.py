def f(i):
    if i<20:
        m=6*i*i+1
        print("%.2f"%m)
    elif i>=40:
        m=100/(i+1)
        print("%.2f"%m)
    else:
        m=(3*i-60)**(1/2)
        print("%.2f"%m)
a=eval(input())
f(a)


