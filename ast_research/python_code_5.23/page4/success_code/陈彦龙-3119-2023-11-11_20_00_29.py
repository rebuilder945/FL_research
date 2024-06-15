lsts = eval(input())
lst2 = []
for x in lsts[::-1]:
    if x not in lst2:
        lst2.append(x)
print(lst2[::-1])

