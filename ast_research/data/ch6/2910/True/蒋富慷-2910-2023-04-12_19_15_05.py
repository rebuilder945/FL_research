h = eval(input())
n = eval(input())
sum = h
for x in range(n-1):
    sum = sum + h*(0.5)**x
print('%.2f'%sum)
