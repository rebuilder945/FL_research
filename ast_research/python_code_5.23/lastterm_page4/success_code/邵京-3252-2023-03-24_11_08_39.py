def Fibonacci(listpri,t):
    listpri=[1,1]
    for x in listpri:
        d=listpri[len(listpri)-2]+listpri[len(listpri)-1]
        listpri.append(d)
        if len(listpri)>=t:
            break
        else:
            continue
            y=listpri[t]
    return(y)
     
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


