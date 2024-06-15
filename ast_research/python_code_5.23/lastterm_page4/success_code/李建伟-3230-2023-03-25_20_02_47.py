lst = eval(input())
lst.sort()
sum = 0
n = 0
for i in lst:
    n = n + 1
    sum = sum + i*10**n
print(sum)
