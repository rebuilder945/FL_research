x1=eval(input())
x2=sum(x1)/len(x1)
if type(x2)==int:
    print(x2)
else:
    print("%.2f"%(x2))
