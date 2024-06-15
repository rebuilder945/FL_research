h=int(input())
N=int(input())
a=[]
for i in range(N):
    b=h*0.5**i
    a.append(b)
print("%.2f"%sum(a))
