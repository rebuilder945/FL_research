h=int(input())
N=int(input())
for i in range(N):
        long=[]
        b=0.5**(i-1)
        c=h*b*2
        long.append(c)
print("%.2f"%sum(long))
