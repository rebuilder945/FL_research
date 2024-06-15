a = list(eval(input()))
b = sum(a)/len(a)
c = int(b)
if b-c !=0:
    print("%.2f"%(b))
else:
    print(c)
