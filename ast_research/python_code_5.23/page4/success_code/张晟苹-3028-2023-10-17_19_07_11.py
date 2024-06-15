a,b,c=eval(input())
d=[]
d.append(a)
for i in range(b-1):
    a+=c
    d.append(a)
print(d)
