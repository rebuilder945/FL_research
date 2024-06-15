def color(n):
    if n==0:
        return("green")
    elif n in range(1,11):
        if n%2==0:
            return("black")
        else:
            return("red")
    elif n in range(11,19):
        if n%2==0:
            return("red")
        else:
            return("black")
    elif n in range(19,29):
        if n%2==0:
            return("black")
        else:
            return("red")
    elif n in range(29,37):
        if n%2==0:
            return("red")
        else:
            return("black")
    else:
        return("error")
a=eval(input())
b=color(a)
print(b)
