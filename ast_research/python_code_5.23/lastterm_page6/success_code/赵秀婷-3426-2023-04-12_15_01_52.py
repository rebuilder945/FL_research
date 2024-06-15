a = eval(input())
if a < 20:
    result = 6*a**2+1
elif 20 <= a < 40:
    result = (3*a-60)**(1/2)
elif a >= 40:
    result = 100/(a+1)
print("%.2f" %(result))
