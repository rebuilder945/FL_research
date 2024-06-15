a=eval(input())
print(a)
n=-len(a)-1
c=[]
for x in a[0:len(a)-1]:
    n=n+1
    if x  not in a[-1:n:-1]:
        c.append(x)
c.append(a[len(a)-1])
print(c)

