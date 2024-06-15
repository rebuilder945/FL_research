lst = eval(input())
i = 0
for j in range(len(lst)):
    if lst[j] != 0:
        lst[i] = lst[j]
        i += 1
while i < len(lst):
    lst[i] = 0
    i += 1
print(lst)

