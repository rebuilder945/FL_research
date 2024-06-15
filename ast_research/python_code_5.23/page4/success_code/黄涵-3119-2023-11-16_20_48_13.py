lst = eval(input())
lst.reverse()
b = []
for i in lst :
    if i not in b :
        b.append(i)
b.reverse()
print(b)
