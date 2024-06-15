x = float(input())
if x < 20:
    y = 6*x**2+1
    print("%.2f"%y)
elif x >= 20 and x < 40:
    n = 3*x-60
    y = n**0.5
    print("%.2f"%y)
elif x >= 40:
    n = x+1
    y = 100/n
    print("%.2f"%y)
