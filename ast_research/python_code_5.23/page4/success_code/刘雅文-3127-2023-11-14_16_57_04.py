'''a=eval(input())
cubes=[x for x in range(1,a+1)]
b=cubes
f=cubes[0]
for x in range(a-1):
    b[x]=cubes[x+1]
b[a-1]=f
print(b)'''

a=eval(input())
b=[x for x in range(1,a+1)]
m=b[0]
for i in range(len(b)-1):
    b[i]=b[i+1]
b[-1]=m
print(b)
