n = eval(input())
m = [i for i in range(1,n+1)]
l = []
for i in m:
    if i < max(m):
        i %= 1
        l.append(i)
    else:
        i = 1
        l.append(i)
print(m)

