n=eval(input())
cubes=[n for n in range(1,n+1)]
for x in cubes:
    cubes[x-1]=x+1
cubes[n-1]=1
print(cubes)
