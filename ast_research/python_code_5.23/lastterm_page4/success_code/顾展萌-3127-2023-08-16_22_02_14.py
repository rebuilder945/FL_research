n = eval(input())
cubes = [x for x in range(n)]
lst = []
for i in cubes:
    if cubes.index(i) == 0:
        lst.append(i)
    else:
        lst.insert(1,i)
lst.reverse()
print(lst)


