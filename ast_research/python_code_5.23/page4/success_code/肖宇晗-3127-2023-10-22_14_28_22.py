n=eval(input())
cubes = [x for x in range(1,n+1)]
a = cubes.pop(0)
cubes.append(a)
print(cubes)
