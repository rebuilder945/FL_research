
n=eval(input())
shang=2
sum=0
for i in range(1,n+1):
    sum=sum+shang/i
    shang=shang+i
print("%.4f"%(sum))

