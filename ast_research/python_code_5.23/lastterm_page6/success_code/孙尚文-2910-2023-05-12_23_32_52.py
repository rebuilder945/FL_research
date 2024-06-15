h=eval(input())
N=eval(input())
a=h
for i in range(1,N):
    a+=2*(h/(2**i))
print("%.2f"%(a))
