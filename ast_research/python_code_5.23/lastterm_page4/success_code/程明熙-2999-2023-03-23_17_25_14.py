c=list(input())
x=list(input())
a=eval(x[0])
b=eval(x[-1])
l=c.split(",")
c[a],c[b]=c[b],c[a]
print(c)
# print(type(a),type(b))
