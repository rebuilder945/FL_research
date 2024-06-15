n=eval(input())
if n <20:
    k=6*n**2+1
elif n<40 and n>=20:
    k=(3*n-60)**0.5
elif n>=40:
    k=(100/(n+1))
print(".2f"%(n))
