a=eval(input())
if 0 in a:
    a.remove(0)
    a.append(0)
print(a)
