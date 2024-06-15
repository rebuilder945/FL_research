n = eval(input())
m = [i for i in range(1,n+1)]
for i in m:
    if i < max(m):
        i += 1
    else:
        i = 1
print(m)

