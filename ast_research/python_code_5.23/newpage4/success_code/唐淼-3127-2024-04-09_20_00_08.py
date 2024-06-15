n=eval(input())
cubes=[x for x in range(1,n+1)]
b=[]
for i in cubes[1:-1]:
    b.append(i)
b.append(1)
print(b)

