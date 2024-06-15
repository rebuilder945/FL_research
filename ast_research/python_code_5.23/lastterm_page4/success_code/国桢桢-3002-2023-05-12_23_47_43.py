l = eval(input())
s = sum(l)
a = s/len(l)
if float(a)<=int(a)+0.01 and float(a)>=int(a)-0.01:
    print(int(a))
else:
    print("%.2f"%(a))
