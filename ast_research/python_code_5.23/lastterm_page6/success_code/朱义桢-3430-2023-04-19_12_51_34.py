def month(n):
    if n in range(3,6):
        return("spring")
    elif n in range(6,9):
        return("summer")
    elif n in range(9,12):
        return("autumn")
    elif n in [12,1,2]:
        return("winter")
    else:
        return("error")
a=eval(input())
b=month(a)
print(b)
