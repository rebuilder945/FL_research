a = eval(input())
lst = []
i = 2
for i in a:
    for b in range(2,i):
        if i%b == 0:
                break
        else:
            lst.append(i)
print(lst)

