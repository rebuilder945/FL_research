n = eval(input())
sum = 0
a = 2
for x in range(n):
    if x == 0:
        sum += 2/1
    else:
        a += x
        sum += (a/(a-x))
print('%.4f'%sum)
