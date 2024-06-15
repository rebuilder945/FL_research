lst = eval(input())
a = len(lst)
for i in range(a):
    if lst[i] != 0:
        j = i+1
        while j < a:
            if lst[j] != 0:
                lst[i] = lst[j]
                lst[j] = 0
                break
            j += 1
print(lst)
