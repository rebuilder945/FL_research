x = input()
a = float(x)
if a<20:
    f = 6*(a**2)+1
elif 20<=a<40:
    f = (3*a-60)**0.5
elif 40<=a:
    f = 100/a+1
print("%.2f"%f)

