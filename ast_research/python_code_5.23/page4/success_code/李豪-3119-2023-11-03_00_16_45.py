def shanchu(a):
    a=eval(input())
    for i in a:
        if i in a.remove(i):
            a.remove(i)
            return(a)
        print(a)             

      
