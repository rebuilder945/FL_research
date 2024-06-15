def caculate(x):
    if x < 20:
        w = 6*(2**x)+1
    if 20 <= x < 40:
        w = 0.5**(3*x-60)
    if 40 <= x:
        w = 100/(x+1)
        
    return w

a=eval(input())
b = caculate(a)
print("%.2f"%b)
