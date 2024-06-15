nml=(input().split(","))
n=eval(nml[0])
m=eval(nml[1])
l=eval(nml[2])
cubes=[n+i*l for i in range(m)]
print(cubes)
