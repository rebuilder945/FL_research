lista = eval(input())
for x in lista:
    if x == 0:
        lista.remove(x)
        lista.append(x)
print(lista)
