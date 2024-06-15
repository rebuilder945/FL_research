a = eval(input())
lst = []
if 2 in a:
    lst.append(2)
else:
    for i in a:
        for b in range(3,i):
            if i%b == 0:
                break
            else:
                lst.append(i)
                break
print(lst)

