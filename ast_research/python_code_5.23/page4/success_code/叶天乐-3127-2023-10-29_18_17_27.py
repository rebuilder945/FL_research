n = int(input())
ls1 = [x+1 for x in range(0,n)]
for x in range(2,n):
    ls1[n-1] = ls1[n]
ls1[n] = 1
print(ls1)
