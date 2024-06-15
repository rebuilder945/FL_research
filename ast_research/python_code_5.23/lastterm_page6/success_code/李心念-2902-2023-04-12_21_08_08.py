x = eval(input())
n = [1,2]
for y in range(x-1):
    n.append(n[y]+n[y+1])
m = [n[(z+1)]/n[z] for z in range(len(n)-1)]
print('%.4f'%sum(m))
