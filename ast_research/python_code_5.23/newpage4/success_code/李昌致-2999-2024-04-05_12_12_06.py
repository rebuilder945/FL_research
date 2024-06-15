a = input()
b = input()
lista = a.split(' ')
listb = b.split(' ')
n,m = int(listb[0]),int(listb[1])
x,y = lista[n],lista[m]
del lista[n]
lista.insert(n,y)
del lista[m]
lista.insert(m,x)
print(lista)
