a=eval(input())
b=sum(a)/len(a)
c=str(b)
if c[-1] in ["0"]:
    print(int(b))
else:
    print("%.2f"%(b))

