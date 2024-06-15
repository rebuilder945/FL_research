lst = eval(input())
lst2 = []
l = len(lst) - 1
sum1 = 0
for i in range(len(lst)):
    for i in range(len(lst)):
        n = max(lst)
        lst2.append(n)
        sum1 = sum1 + n*10**l
        l -=1
        lst.remove(n)
print(sum1)

