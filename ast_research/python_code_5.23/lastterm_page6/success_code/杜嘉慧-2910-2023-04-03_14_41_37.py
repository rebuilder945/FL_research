h,N=eval(input())
sums=h
for x in range(N-1):
    sums+=h*0.5**x
print("%.2f"%(sums))

