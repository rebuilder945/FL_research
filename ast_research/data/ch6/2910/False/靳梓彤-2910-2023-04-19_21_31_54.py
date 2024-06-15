h=int(input())
N=int(input())
for i in range(2,N+1):
        long=[h]
        b=0.5**(i-1)
        c=2*(h*b)
        long.append(c)
print("%.2f"%sum(long))
