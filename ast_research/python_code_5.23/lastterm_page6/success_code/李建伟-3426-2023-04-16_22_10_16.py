x = eval(input())
if x < 20:
    f = 6*x*x+1
elif 20 <= x < 40:
    f = (3*x-60)**0.5
else:
    f = 100/(x+1)
print("%.2f"%(f))
