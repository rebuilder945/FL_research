a=list(input().split(","))
x=int(a[0])
y=int(a[1])
z=int(a[2])
b=[]
for i in range(x,y*z+x-y,z):
    b.append(i)
print(b)
