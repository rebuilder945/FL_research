a = eval(input())
b = sum(a)/len(a)
if b is int:
    print(b)
if b is float:
    print("%.2f"%(b))

