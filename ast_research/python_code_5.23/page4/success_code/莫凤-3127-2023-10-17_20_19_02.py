a=eval(input())
cubes=[x for x in range(1,a+1)]
b=cubes.pop()
cubes.insert(0,b)
print(cubes)
