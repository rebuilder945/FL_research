Nums=eval(input())
a=sum(Nums)
b=len(Nums)
c=a/b
if b%a:
    print("%d"%(c))
if not b%a:
    print("%.2f"%(c))
