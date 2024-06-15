lst = eval(input())
seen = set()
new_lst = []
for x in lst:
    if x not in seen:
        seen.add(x)
        new_lst.append(x)
print(new_lst)

