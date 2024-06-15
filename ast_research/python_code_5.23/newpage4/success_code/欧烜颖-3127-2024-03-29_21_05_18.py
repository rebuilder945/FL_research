n = eval(input())
cubes = [x for x in range(1,n+1)]
for m in cubes:
    if m == 1:
        cubes.remove(1)
        cubes.append(1)
    else:
        break
print(cubes)
