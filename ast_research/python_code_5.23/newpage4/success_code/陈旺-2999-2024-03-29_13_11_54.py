a=input()
m,n=eval(input())
lista=[str(i) for i in a.split(",")]
t=lista[n]
f=lista[m]
lista[m]=t
lista[n]=f
print(lista)


