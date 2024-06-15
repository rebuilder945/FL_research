lista = eval(input())
n =len(lista)
listb = []
for a in range(n-1,-1,-1):
    listb.append(lista[a])
    if listb.count(lista[a])>1:
        c = len(listb)
        del listb[c-1]
listb.reverse()
print(listb)
