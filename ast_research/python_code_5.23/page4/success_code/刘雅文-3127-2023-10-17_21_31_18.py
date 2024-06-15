a=eval(input())
cubes=[x for x in range(1,a+1)]
b=cubes
for x in range(a-1):
    b[x]=cubes[x+1]
    b[a-1]=cubes[0]
print(b)
