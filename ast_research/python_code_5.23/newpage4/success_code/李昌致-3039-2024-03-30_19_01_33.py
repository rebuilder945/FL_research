a = eval(input())
maximum = max(a)
minimum = min(a)
i = 0
while i <= len(a):
    while a[i] == maximum or a[i] == minimum:
        del a[i]
    i = i+1
print(a)
