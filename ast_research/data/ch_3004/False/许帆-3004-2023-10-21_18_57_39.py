a = eval(input())
lst = []
for i in a:
    for b in range(2,i):
        if i%b == 0:
                break
        else:
            lst.append(i)
print(lst)

