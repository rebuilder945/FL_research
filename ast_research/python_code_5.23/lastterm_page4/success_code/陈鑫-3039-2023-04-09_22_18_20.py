a=eval(input())
for b in a:
    if b==min(a) or b==max(a):
        for i in range(a.count(b)):
            a.remove(b)
    break
print(a)
