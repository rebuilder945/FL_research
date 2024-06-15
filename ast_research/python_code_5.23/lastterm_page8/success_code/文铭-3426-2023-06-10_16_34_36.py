x = eval(input())
if x < 20:
    js =6*x**2+1
    print("%.2f"%js)
elif 20<= x< 40:
    js = (3*x-60)**0.5
    print("%.2f"%js)
else:
    js=100/(x+1)
    print("%.2f"%js)
