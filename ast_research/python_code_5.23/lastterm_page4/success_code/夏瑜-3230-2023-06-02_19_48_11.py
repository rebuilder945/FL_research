a=eval(input())
a.sort(reverse=True)
b=[]
print(a)
for i in range(0,len(a)):
    c=a[i]*10**(len(a)-i-1)
    b.append(c)
d=sum(b)
print(d)
