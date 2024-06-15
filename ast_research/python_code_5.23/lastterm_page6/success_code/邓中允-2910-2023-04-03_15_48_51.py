height=eval(input())
N=eval(input())
m=height
for i in range(N-1):
    m+=height*(0.5)**i
print("%.2f"%m)
