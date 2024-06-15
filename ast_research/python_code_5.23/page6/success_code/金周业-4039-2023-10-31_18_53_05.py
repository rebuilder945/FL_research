n=eval(input())
m=0
if n<20:
    m=6*(n**2)+1
elif 20<=n and n<40:
    m=(3*n-60)**0.5
elif n>=40:
    m=100/(n+1)
print("%.2f"%m)

