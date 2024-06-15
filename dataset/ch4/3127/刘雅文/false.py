a=eval(input())
cubes=[x for x in range(1,a+1)]
b=cubes
print(b)
f=cubes[0]
for x in range(a-1):
    b[x]=cubes[x+1]
b[a-1]=f
print(b)
