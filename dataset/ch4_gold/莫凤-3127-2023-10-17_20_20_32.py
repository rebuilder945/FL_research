a=eval(input())
cubes=[x for x in range(1,a+1)]
b=cubes.pop(0)
cubes.append(b)
print(cubes)
