a = eval(input())
lst = []
if 2 in a:
    lst.append(2)
    a.remove(2)
for i in a:
    for b in range(2,i):
        if i%b == 0:
            break
        else:
            lst.append(i)
            break
print(lst)

