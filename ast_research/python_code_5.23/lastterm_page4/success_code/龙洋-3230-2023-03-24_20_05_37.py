cubes=eval(input())
n=len(cubes)
cubes.sort()
x=[cubes[x]*10**x for x in range(n)]
print(sum(x))

