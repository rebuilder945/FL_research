sum = eval(input())
sumas = sum.copy()
for x in sum:
    a = sum.count(x)
    if a >= 1:
        for i in range(a-1):
            sumas.remove(x)
print(sumas)
