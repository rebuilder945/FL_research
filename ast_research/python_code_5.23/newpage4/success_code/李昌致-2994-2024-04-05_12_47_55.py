list = input()
n,m = eval(input())
n = int(n)
m = int(m)
lista = list.split(',')
if n < 0:
    n = len(list)+n

if n>= 0 and n<len(list):
    a = lista[n]
    for i in range(m):
        lista.append(a)
    for x in range(len(lista)):
        b = int(lista[x])
        del lista[x]
        lista.insert(x,b)
    print(lista)
else:
    print("error")
