def calculate(maxn,s=0,a=1,b=2,n=0):
    if n==maxn : return s
    else: return(calculate(maxn,s+a/b,a+b,a,n+1))

n=int(input())
print(f"{calculate(n):.4f}")
