s=input()
a,b= s.split(",")
a=float(a)
b=float(b)
q=input()
c,d= q.split(',')
c=float(c)
d=float(d)
D=((a-c)**2+(b-d)**2)**0.5
D="%.2f" % D
print(D)

