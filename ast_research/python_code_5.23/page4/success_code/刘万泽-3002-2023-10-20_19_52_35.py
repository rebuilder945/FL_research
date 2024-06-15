a=eval(input())
b=sum(a)
c=sum(a)/len(a)
t=c.floor()
if c>t:
    print("%.2f"%(c))
else:
    print(int(c))    
