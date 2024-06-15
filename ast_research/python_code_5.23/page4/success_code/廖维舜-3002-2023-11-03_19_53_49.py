a=eval(input())
x=sum(a)/int(len(a))
if type(x)==int:
    print("%.d"%(x))
else:
    print("%.2f"%(x))

