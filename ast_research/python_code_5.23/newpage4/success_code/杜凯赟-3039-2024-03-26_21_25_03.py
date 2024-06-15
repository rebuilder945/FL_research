a = eval(input())
maxa = max(a)
mina = min(a)
if maxa in a:
    a.remove(maxa)
if mina in a:
    a.remove(mina)
print(a)
