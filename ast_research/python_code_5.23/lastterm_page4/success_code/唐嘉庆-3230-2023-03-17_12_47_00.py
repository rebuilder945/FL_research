a=eval(input())
a.sort(reverse=False)
c=[]
for i in range(len(a)):
    x=a[i]*(10**(i))
    c.append(x)
print(sum(c))
