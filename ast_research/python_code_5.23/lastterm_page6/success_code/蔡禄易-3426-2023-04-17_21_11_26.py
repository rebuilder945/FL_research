x = eval(input())
if x<20:
    a = 6*x*x+1
elif 20<=x<40:
    n = 3*x-60
    a = n.sqrt(n)
else:
    a = 100/(x+1)
print(a)
