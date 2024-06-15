c=input()
x=list(input())
a=x[1]
b=x[-1]
l=c.split(",")
c[a],c[b]=c[b],c[a]
print(c)

