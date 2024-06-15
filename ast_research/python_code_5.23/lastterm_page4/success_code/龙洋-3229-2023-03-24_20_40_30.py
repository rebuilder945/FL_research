cubes=eval(input())
p=','
lis=[]
for x in cubes:
    if cubes.count(x)==1:
        lis.append(x)
if not lis:
    print("False")
else:
    lis.sort()
    list=[str(y) for y in lis]
    print(p.join(list))

