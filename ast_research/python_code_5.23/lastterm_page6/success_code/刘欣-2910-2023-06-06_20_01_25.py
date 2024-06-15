height=int(input())
n=int(input())
sum1=height
lis=[height]
sum2=0
for i in range(n-1):
    sum1*=0.5
    lis.append(sum1*2)
for i in lis:
    i=float(i)
    sum2+=i
print("%.2f"%sum2)
