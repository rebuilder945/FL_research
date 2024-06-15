n=eval(input())
cubes=[x for x in range (1,n+1)]
for i in range(1):
    num=cubes.pop(0)
    cubes.append(num)
print(cubes)
