a=input().split()
b=a[1:]
b.sort()
c=".00"
d=[]
for i in b:
    i+=c
    d.append(i)
e=eval(b[0])+eval(b[1])+eval(b[2])
a[1:4]=d[:]
a.append((str(e/len(d)))+"0")
x=" ".join(map(str,a))
print(x)

