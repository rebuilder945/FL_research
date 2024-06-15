list = input()
n,m = eval(input())
n = int(n)
m = int(m)
lista = list.split(',')
if n < 0:
    n1 = len(list)+n
else:
    n1 = n

if n1>= 0 and n1<len(list):
    a = lista[n1]
    for i in range(m):
        lista.append(a)
    for x in range(len(lista)):
        b = int(lista[x])
        del lista[x]
        lista.insert(x,b)
    print(lista)
else:
    print("error")
