a = eval(input())
if a < 20:
    b = 6*(a**2)+1
    print("%.2f"%b)
elif 20<= a <40:
    b = (3*a-60)**0.5
    print("%.2f"%b)
else:
    b = 100/(a+1)
    print("%.2f"%b)
