a=eval(input())
d=sum(a)/len(a)
if d//1==d/1:
    print(int(d//1))
else:
    print("%.2f"%(d))
