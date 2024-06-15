lst = eval(input())
lst.sort()
print(lst)
sum = 0
for i in lst:
    n = lst.index(i)
    sum = sum + i*10**n
print(sum)
