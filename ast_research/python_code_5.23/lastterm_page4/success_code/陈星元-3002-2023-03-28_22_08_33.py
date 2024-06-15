list=eval(input())
a=sum(list)/len(list)
b=str(a)
c=b.split(".")
if int(c[-1])!=0:
    print("%.2f"%(a))
else:
    print(int(a))

