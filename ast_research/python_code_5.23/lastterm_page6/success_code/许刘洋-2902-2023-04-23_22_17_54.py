n=int(input())
n_sum=0
a=1
b=2
for i in range (n):
    n_sum+=b/a
    a,b=b,a+b
print("%.4f"%n_sum)
