l = eval(input())
s = sum(l)
n = len(l)
a = s/n
if a%1==0:
    print(int(a))
else:
    print("%.2f"%a)
