n = int(input())
ls1 = [x+1 for x in range(0,n)]
for x in range(n):
    ls1[x-1] = ls1[x]
ls1[n-1] = 1
print(ls1)
