Nums=eval(input())
a=sum(Nums)
b=len(Nums)
c=a/b
if a//b:
    print("%d"%(c))
else:
    print("%.2f"%(c))
