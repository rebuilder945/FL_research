lst = eval(input())
a = len(lst)
for i in range(a):
    if lst[i] != 0:
        i = i+1
    else:
        del lst[i]
        lst.append(0)
print(lst)
