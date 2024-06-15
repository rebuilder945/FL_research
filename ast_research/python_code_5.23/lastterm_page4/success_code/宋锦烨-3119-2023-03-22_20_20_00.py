a=eval(input())
for i in a.copy():
    if a.count(i) > 1:
        a.remove(i)
print(a)
