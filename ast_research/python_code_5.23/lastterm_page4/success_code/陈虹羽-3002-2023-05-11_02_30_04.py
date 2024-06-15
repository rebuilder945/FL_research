a=eval(input())
b=sum(a)/len(a)
c=sum(a)%len(a)
if c==0: 
    print(b)
else:
    print("%.2f"%(b))

