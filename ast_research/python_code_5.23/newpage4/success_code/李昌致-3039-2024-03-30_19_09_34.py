a = eval(input())
print(a)
maximum = max(a)
minimum = min(a)
i = 0
while i <= (len(a)-1):
    while a[i] == maximum or a[i] == minimum:
        del a[i]
        if i >= len(a):
            break
    i = i+1
print(a)
