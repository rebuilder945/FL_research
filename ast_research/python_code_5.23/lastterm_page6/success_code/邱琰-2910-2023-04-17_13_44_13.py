h=eval(input())
N=eval(input())
lst=[h]
if N==1:
    print("%.2f"%(h))
if N>=2:
    for i in range(1,N):
        x=lst[-1]*0.5**i
        lst.append(x*2)
    a=sum(lst)
    print("%.2f"%(a))
