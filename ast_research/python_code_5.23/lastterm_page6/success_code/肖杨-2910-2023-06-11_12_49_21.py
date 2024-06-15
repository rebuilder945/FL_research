a=eval(input())
N=eval(input())
c=a
b=0
for i in range(N):
    b+=2*a
    a=a/2
print("%.2f"%(b-c))



