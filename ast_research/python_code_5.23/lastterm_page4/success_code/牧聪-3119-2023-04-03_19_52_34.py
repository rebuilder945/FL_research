a=eval(input())
for x in a:
    if x in a[-1:x]:
        a.remove(x)
print(a)

