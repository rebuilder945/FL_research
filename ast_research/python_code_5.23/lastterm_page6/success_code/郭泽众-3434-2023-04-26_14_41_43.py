pCl = {'red','blue','yellow'}
cSt = eval(input())
cNd = eval(input())
if cSt not in pCl or cNd not in pCl or cSt == cNd:
    print('error')
else:
    cLo = {cSt, cNd}
    if cLo == {'red','blue'}:
        print('purple')
    if cLo == {'red','yellow'}:
        print('orange')
    if cLo == {'blue','yellow'}:
        print('green')
