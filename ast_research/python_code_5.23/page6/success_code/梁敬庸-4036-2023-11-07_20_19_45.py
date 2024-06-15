a=eval(input())
if a<0 or a>36:
    print("error")
else:
    if a==0:
        print("green")
    elif a>=0 and a<11:
        if a%2==0:
            print("black")
        else:
            print("red")    
    elif a>=11 and a<19:
        if a%2==0:
            print("red")
        else:
            print("black")
    elif a>=19 and a<29:
        if a%2==0:
            print("black")
        else:
            print("red")
    elif a>=29 and a<37:
        if a%2==0:
            print("red")
        else:
            print("black")
