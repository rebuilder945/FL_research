def jisuan(n):
    if n<20:
        b=6*n**2+1
    elif n<40 and n>=20:
        b=(3*n-60)**0.5
    elif n>=40:
        b=100/(n+1)
    return b
x=eval(input())
print(jisuan(x))
