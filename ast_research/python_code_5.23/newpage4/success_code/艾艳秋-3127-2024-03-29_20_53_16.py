n=eval(input())
cubes=[x for x in range(1,n-1)]
cubes.append(1)
cubes.pop(0)
print(cubes)
