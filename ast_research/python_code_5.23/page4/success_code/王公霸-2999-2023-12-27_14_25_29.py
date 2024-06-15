lista = list(input().split(" "))
n,m = map(int,input().split(" "))
a = lista[m]
b = lista[n]
lista[n] = a
lista[m] = b
print(lista)
