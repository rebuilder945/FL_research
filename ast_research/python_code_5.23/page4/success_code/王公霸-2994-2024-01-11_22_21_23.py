lista = [int(i) for i in input().split(',')]
n,m =input().split(",")
n = int(n)
m = int(m)
t =0
if abs(n)+1>len(lista):
    print("error")
elif abs(n)+1<=len(lista):
    listc = lista[n]
    for t in range(0,m):
        lista.append(listc)
        t+=1
    print(lista)
