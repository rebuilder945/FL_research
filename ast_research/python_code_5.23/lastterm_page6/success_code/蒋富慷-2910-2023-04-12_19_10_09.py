h = eval(input())
n = eval(input())
sum = h
for x in range(n-1):
    h = h*(0.5)**x
    sum = sum + h
print(sum)
