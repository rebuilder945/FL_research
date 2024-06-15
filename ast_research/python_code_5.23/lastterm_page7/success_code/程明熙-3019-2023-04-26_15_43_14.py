a=input().split()
b=a[1:]

c=".00"
d=[]
for i in b:
    i+=c
    d.append(eval(i))
d.sort(reverse=True)
print(d)
e=eval(b[0])+eval(b[1])+eval(b[2])
a[1:4]=d[:]
a.append("%.2f"%(e/len(d)))
x=" ".join(map(str,a))
print(x)

