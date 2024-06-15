oplist = []
num = int(input())
for i in range(100,num + 1):
    stri = str(i)
    a = int(stri[0])
    b = int(stri[1])
    c = int(stri[2])
    udi = a ** 3 + b ** 3 + c **3
    if udi == i:
        oplist.append(str(i))
if len(oplist) == 0:
    print('none')
else:
    print('\n'.join(oplist))
