h=eval(input())
n=eval(input())
sums=[h]
for i in range(1,n):
    h=h*(0.5)
    sums.append(2*h)
   
summary=sum(sums)
print("%.2f"%(summary))
