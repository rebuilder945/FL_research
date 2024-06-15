
n=eval(input())
shang=2
xia=1
sum=0
for i in range(n):
    sum=sum+shang/xia
    shang,xia=shang+xia,shang
print("%.4f"%(sum))

