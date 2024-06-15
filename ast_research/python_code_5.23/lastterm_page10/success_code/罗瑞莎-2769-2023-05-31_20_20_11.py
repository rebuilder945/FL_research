a = input()
print(''.join(a))
lst = []
for x in a:
    lst.append(x)
a1 = 'abcdefghijklmnopqrstuvwxyz'
a2 = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a3 = 'zyxwvutsrqponmlkjihgfedcba'
a4 = 'ZYXWVUTSRQPONMLKJIHGFEDCBA'
for i in range(len(lst)):
    if lst[i].isalpha:
        if lst[i] in a1:
           lst[i] = a3[a1.index(lst[i])]
        elif lst[i] in a2:
            lst[i] = a4[a2.index(lst[i])]
print(''.join(lst))
