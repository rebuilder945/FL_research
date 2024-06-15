a=input()
b=[int(i) for i in input().split(" ")]
m=b[0]
n=b[1]
lista=[str(i) for i in a.split(",")]
t=lista[n]
f=lista[m]
lista[m]=t
lista[n]=f
print(lista)


