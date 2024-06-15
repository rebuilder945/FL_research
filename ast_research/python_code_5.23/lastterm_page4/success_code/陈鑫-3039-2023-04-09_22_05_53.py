a=eval(input())
for b in a:
    if b==min(a):
        a.remove(b)
    break
for b in a:
    if b==max(a):
        a.remove(b)
    break
print(a)
