a=eval(input())
big=max(a)
small=min(a)
n=a.count(big)
m=a.count(small)
for i in range(n):
    if big in a:
        a.remove(big)
for i in range(m):
    if small in a:
        a.remove(small)
print(a)
