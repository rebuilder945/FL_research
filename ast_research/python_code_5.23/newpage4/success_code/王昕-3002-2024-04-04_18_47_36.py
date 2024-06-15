n=eval(input())
c=sum(n)%len(n)
b=sum(n)/len(n)
if c==0:
    print(int(b))
elif c!=0:
    print("%.2f"%(b))
     
