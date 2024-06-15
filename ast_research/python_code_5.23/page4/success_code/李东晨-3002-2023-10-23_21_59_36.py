a=eval(input())
b=sum(a)/len(a)
if b%1!=0:
    print("%.2f"%(b))
else:
    print(int(b))
