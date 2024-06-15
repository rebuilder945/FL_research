l = eval(input())
t = len(l)
n = sum(l)
a = n/t
b = float(a)
if b>0:
    print("%.2f"%(a))
elif b==0:
    print(int(a))
