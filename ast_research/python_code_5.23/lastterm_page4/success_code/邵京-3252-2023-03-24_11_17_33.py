def Fibonacci(listpri,t):
    for x in listpri:
        d=listpri[len(listpri)-2]+listpri[len(listpri)-1]
        listpri.append(d)
        if len(listpri)==t:
            break
        else:
            continue
    return(listpri[t-1])
    
     
    




num = [1, 1]
n = int(input())
print(Fibonacci(num, n))


