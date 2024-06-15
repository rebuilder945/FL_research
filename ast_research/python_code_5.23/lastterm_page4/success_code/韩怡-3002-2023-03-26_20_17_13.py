a=eval(input())
x=sum(a)/len(a)
y=sum(a)%len(a)
if y ==0:
    print("%d"%(x))
else:
    print("%.2f"%(x))


