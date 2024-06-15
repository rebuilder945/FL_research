a=eval(input())
for b in a:
    if b==min(a):
        a.remove(b)
        for b in a:
            if b in a:
                a.remove(b)
            else:
                pass
    break
for b in a:
    if b==max(a):
        a.remove(b)
        for b in a:
            if b in a:
                a.remove(b)
            else:
                pass
    break
print(a)
