dic={}
a,b,c,d=input().split()
b,c,d="{b:.2f} {c:.2f} {d:.2f}".format(b=int(b),c=int(c),d=int(d)).split()
lst1=sorted([b,c,d],key=lambda x :float(x),reverse=True)
o=(float(b)+float(c)+float(d))/3
x="{:.2f}".format(o)
lst1.insert(0,a)
lst1=lst1+[x]
print(*lst1,end=" ")
