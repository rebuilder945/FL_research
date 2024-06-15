lista = eval(input())
a=0
b=a+1
while a>=len(lista)-1:
    x = lista[a]
    while b>=len(lista):
        y = lista[b]
        b+=1
        if x==y:
            lista.pop(a)
            break
    a+=1
print(lista)
