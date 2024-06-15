a=eval(input())
p=sum(a)/len(a)
b=int(p)
if p-b==0:
    print(b)
else:
    print("%.2f"%p)
