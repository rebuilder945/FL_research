lista = eval(input())
listb = []
for i in lista:
    if lista.count(i)<=1:
        listb.append(i)
if listb==[]:
    print("False")
else:
    listb.sort(reverse=False)
    h = ','.join(str(x) for x in listb)
    print(h)
