list=eval(input())
x=sum(list)
a=x/len(list)
b=int(a)
if a-b==0:
    print("%d"%(a))
else:
    print("%.2f"%(a))
