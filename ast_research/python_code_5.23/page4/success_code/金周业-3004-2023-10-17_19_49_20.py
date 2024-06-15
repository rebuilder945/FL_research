def sushu(lista):
    for i in range(len(lista)):
        for j in range(2,int(lista[i]**0.5)):
            if lista[i] % j == 0:    
                del lista[i]
                break
    return lista
listb=eval(input())
print(sushu(listb))


                

