lst = input()
a = max(lst)
b = min(lst)
for x in [a,b]:
    if x in lst:
        lst.remove(x)
    else:
        pass
print(lst)
