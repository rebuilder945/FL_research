n=eval(input())
if n<20:
    sum=6*n**2+1
elif 20<=n<40:
    sum=(3*n-60)**0.5
else:
    sum=100/(n+1)
print("%.2f"%sum)


