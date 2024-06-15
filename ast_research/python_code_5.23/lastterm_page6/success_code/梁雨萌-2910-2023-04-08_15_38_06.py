high=eval(input())
N=eval(input())
h=high/2
if N==1:
    print(high)
else:
    for i in range(2,N+1,1):
        high=high+h*2
        h=h/2
    print("%.2f"%high)
