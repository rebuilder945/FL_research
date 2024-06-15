a = eval(input())
b = sum(a)/len(a)
if b-int(b) !=0:
    print("%.2f"%(b))
else:
    print(int(b))
