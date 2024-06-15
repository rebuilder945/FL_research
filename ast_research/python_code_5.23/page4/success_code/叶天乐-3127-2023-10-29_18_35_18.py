n = int(input())
ls1 = [x+1 for x in range(0,n+1)]
for x in range(n+1):
    ls1[x-1] = ls1[x]
print(ls1)
