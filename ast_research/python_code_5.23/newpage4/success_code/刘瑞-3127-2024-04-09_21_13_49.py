a=eval(input())
cubes=[i for i in range(1,a+1)]
for x in cubes:
    if x==1:
        cubes.remove(x)
        cubes.append(x)
print(cubes)            
