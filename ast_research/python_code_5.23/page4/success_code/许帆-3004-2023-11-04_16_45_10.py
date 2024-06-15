a = input().split()
b = 2
lst = []
if 2 in a:
    lst.append(2)
    a.remove(2)
for i in range(len(a)):
    for x in range(a[i]-3):
        if b < a[i] and a[i]/b == 0:
            break
        elif b < a[i] and a[i]/b != 0:
            b += 1
        elif b == a[i]-1:
            lst.append(i)
print(lst)



    
print(lst)

