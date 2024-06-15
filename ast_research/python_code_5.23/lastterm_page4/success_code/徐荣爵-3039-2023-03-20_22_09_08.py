lst = eval(input())
a = max(lst)
b = min(lst)
a1 = lst.count(a)
b1 = lst.count(b)
for i in range(a1):
    for i in range(a1):
        if a in lst:
            lst.remove(a)
        else:
            pass
for i in range(b1):
    for i in range(b1):
        if b in lst:
            lst.remove(b)
        else:
            pass    
print(lst)
