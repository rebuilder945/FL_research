a=eval(input())
big=max(a)
small=min(a)
while big in a:
    a.remove(big)
while small in a:
    a.remove(small)
print(a)
