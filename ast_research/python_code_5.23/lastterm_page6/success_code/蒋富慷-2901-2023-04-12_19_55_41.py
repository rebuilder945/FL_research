n = 0
s = 0
m = 1
while(m):
    a = input()
    if a !='#':
        n += 1
        s += a
    else:
        m = 0
print(n,s)
