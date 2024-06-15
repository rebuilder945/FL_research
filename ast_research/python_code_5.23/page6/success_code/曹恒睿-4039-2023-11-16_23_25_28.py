def fenduanhanshu(n):
    if n < 20:
        y = 6*(n**2)+1
        return y
    elif 20 <= n <40:
        y = (3*n-60)**0.5
        return y
    elif n >= 40:
        y = 100/(n+1)
        return y
n = eval(input())
print("%.2f"%(fenduanhanshu(n)))
