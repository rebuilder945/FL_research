x = eval(input())
if x < 20 :
    x = 6*pow(x,2) + 1
elif 20 <= x < 40 :
    x = pow(3*x-60,1/2)
else :
    x = 100 / ( x + 1 )
print("%.2f"%(x))
