b=input()
a=[]
while b!='q':
    a.append(b)
    b=input()
c=[0]*len(a)
for i in range(len(a)):
    c[i]=a.count(a[i])
l=dict(zip(a,c))
h=max(l)
print(h,l[h])
