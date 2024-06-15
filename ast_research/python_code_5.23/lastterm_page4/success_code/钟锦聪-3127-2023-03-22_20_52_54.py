n = int(input())
cubes = [x for x in range(1,n+1)]
cubes.remove(1)
cubes.append(1) 
print(cubes)
