lst = eval(input())
lst.sort()
sum = 0
n = 0
for i in lst:
    sum = sum + i*10**n
    n = n + 1
print(sum)
