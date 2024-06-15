l=eval(input())
i=(l.copy()).count(0)
for k in range(i):
    l.remove(0)
for o in range(i):
    l.append(0)
print(l)

