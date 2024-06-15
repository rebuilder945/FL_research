N=int(input())
  # 第n项:F[-3]
F=[1,1]
for i in range(0,N):
    F.append(int(F[i])+int(F[i+1]))
#分子倒数第2个 分母倒数第3个，列表元素比N多两个
sum=0
for t in range(1,N+1):
    a=F[t+1]/F[t]
    sum+=a
print("%.4f"%(sum))
