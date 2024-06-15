lst = eval(input())
for k in range(len(lst)):
    for i in range(len(lst) - 1):
        if lst[i] == 0:
            lst[i] , lst[i+1] = lst[i+1] , lst[i]
print(lst)



