h=eval(input())
N=eval(input())
i=1
jieguo=1
n=1
while n<=N-1:
    jieguo=jieguo*i
    i=i*(1/2)
    n=n+1
print("%.2f"%jieguo+1)
