sum = eval(input())
for x in sum:
    a = sum.count(x)
    if a > 1:
        for i in range(a-1):
            sum.remove(x)
print(sum)

