a=eval(input())
for b in a:
    if b==min(a):
        for i in range(a.count(b)):
            a.remove(b)
    break
for b in a:
    if b==max(a):
        for i in range(a.count(b)):
            a.remove(b)
    break
print(a)
