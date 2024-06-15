a=list(input())
a1=a[:]
b=eval(input())
b1=b[:]
c=[]
for i in range(len(a)):
    c.append([a1[i],b1[i]])
print(c)

