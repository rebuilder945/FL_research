h = eval(input())
n = eval(input())
sum = h
if n == 1:
    print("%.2f"%(sum))
else:
    for i in range(1,n):
        sum = sum+(h/2**i)*2
    print("%.2f"%(sum))

