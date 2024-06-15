a = input().split()
b = 2
lst = []
if 2 in a:
    lst.append(2)
    a.remove(2)
for i in a:
    for x in range(i-3):
        if b < i and i/b == 0:
            break
        elif b < i and i/b != 0:
            b += 1
        elif b == i-1:
            lst.append(i)
print(lst)



    
print(lst)

