lst = eval(input())
s = len(lst)
for i in range(s):
    if lst[i] != 0:
        i += 1
    elif lst[i] == 0:
        del lst[i]
        lst.append(0)
print(lst)
