x,y,z = input().split(",")
x = int(x)
y = int(y)
z = int(z)
list = [x for x in range(x,x+(y-1)*z+1,z)]
print(list)

