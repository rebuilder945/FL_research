def dengcha(n,m,l):
    kong=[]
    for i in range(m):
        kong.append(n+i*l)
    return kong
n,m,l=eval(input())
result=dengcha(n,m,l)
print(result)
