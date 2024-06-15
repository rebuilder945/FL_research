high=float(input())
n=float(input())
length=high
for x in range(2,n+1):
    high=high*0.5
    length+=2*high
print("%.2f"%length)


