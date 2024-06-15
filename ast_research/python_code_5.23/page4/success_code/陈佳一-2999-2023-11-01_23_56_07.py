a=input()
e=input()
f=e.split(" ")
b=a.split(" ")
c=int(f[0])
d=int(f[1])
b[c],b[d]=b[d],b[c]
print(b)
