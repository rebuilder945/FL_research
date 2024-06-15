def Fibonacci(listpri,t):
    for x in listpri:
        listpri=[1,1]
        d=listpri[len(listpri)-2]+listpri[len(listpri)-1]
        listpri.append(d)
        if len(listpri)>=t:
            break
            y=listpri[t]
        else:
            continue
    return(y)
     
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


