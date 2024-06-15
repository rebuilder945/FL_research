a = input()
a1 = [int(x) for x in a.split(',')]
x = a1[0]
y = a1[1]
z = a1[2]
x1 = x+(y-1)*z+1
n = [x for x in range(x,x1,z)]
print(n)
