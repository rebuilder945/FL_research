l = eval(input())
t = len(l)
n = sum(l)
a = n/t
if int(a)-a==0:
    print(int(a))
else:
    print("%.2f"%(a))
