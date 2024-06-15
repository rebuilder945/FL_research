a=eval(input())
a.sort(reverse=True)
b=len(a)
c=[]
for i in range(b):
    x=a[i]
    x=x*10**(b-i-1)
    c.append(x)
f=sum(c)
print(f)
