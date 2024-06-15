dummy = eval(input())
for x in dummy:
    while dummy.count(x) > 1:
        dummy.remove(x)
print(dummy)
