a=eval(input())
b=eval(sum(a)/len(a))
if b.count(".")==1:
    print("%.2f"%b)
else:
    print(int(b))

