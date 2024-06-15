def dubo(n):
    if n<0 or n>36:
        return("error")
    if n==0:
        return("green")
    if n>0 and n<11:
        if n%2==0:
            return("black")
        else:
            return("red")
    if n>10 and n<19:
        if n%2==0:
            return("red")
        else:
            return("black")
    if n>18 and n<29:
        if n%2==0:
            return("black")
        else:
            return("red")
    if n>28 and n<37:
        if n%2==0:
            return("red")
        else:
            return("black")
a=eval(input())
print(dubo(a))

