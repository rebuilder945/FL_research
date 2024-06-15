a=eval(input())
lt=[]
m=max(a)
n=min(a)
for i in a:
    if i!=m and i!=n:
        lt.append(i)
print(lt)
