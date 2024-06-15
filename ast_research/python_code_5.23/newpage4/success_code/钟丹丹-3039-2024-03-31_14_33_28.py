n = eval(input())
a=max(n)
b=min(n)
c=[]
if a!=b:
    for x in n:
        if x!=a and x!=b:
            c.append(x)
    print(c)
elif a==b:
    print("[]")
