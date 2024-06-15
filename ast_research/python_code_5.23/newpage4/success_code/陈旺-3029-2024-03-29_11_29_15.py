a=input()
b=input()
lista=[str(i) for i in a.split(",")]
b=b.strip("[")
b=b.rstrip("]")
listb=[eval(i) for i in b.split(",")]
m=[]
for i in lista:
    list=[i,listb[lista.index(i)]]
    m.append(list)
print(m)
