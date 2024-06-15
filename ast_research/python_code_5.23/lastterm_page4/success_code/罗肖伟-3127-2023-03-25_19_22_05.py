n=eval(input())
cubes=[x for x in range(1,n+1)]
cubes1=cubes[:]
for i in range(len(cubes)):
    cubes1[i-1]=cubes[i]
print(cubes1)
