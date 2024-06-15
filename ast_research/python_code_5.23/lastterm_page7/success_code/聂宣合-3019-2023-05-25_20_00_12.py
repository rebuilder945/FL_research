s=input().split(" ")
x=[]
a=str(s[0])
b=int(s[1])
c=int(s[2])
d=int(s[3])
avg=(d+b+c)/3
x.append(b)
x.append(c)
x.append(d)
x.sort(reverse=True)
b=x[0]
c=x[1]
d=x[2]
print(a,"%.2f %.2f %.2f %.2f"%(b,c,d,avg))
