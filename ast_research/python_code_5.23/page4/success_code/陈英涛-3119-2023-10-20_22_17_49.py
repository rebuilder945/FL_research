l1 = eval(input())
l1.reverse()
l2 = []
for i in l1:
    if i not in l2:
        l2.append(i)
l2.reverse()
print(l2)
