def hanshu(x) :
    if x<20 :
        a = 6*x**2+1
    elif 20<=x<40 :
        a = (3*x-60)**(1/2)
    else :
        a = 100/(x+1)
    return a
a = eval(input())
print("%.2f"%hanshu(a))
