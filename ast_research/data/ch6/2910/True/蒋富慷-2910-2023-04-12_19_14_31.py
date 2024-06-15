h = eval(input())
n = eval(input())
sum = h
for x in range(n-1):
    a = h*(0.5)**x
    sum = sum + a
print('%.2f'%sum)
