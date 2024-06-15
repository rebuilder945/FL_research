a=eval(input())
m=max(a)
n=min(a)
b=[]
for x in a:
    if x!=m and x!=n:
        b.append(x)
print(b)
