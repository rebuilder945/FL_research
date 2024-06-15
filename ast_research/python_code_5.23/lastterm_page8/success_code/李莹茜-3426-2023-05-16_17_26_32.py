#分段函数求值
a=eval(input())
n=int(a)

if a<20:
    m=6*a**2 +1
elif a>=20 and a<40:
    m=(3*a-60)**0.5
elif a>=40:
    m=100/(a+1)

print("%.2f"% m)
