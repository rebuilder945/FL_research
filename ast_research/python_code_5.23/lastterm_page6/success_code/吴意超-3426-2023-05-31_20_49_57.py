n = eval(input())
if n < 20 :
    a = 6 * n **2 + 1
    print("%.2f"%(a))
elif n >= 20 and n <40 :
    b = (3*n - 60) ** 0.5
    print("%.2f"%(b))
else :
    c = 100 / ( n + 1)
    print("%.2f"%(c))
