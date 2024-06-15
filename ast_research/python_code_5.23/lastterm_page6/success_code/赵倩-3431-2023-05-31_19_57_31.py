a=eval(input())
if a>=37:
    print("error")
elif a in range(0,37):
    if a==0:
        print("green")
    elif (a in range(1,11))or(a in range(19,29)) :
        if a%2==0:
            print("black")
        else:
            print("red")
    elif (a in range(11,19))or(a in range(29,37)):
        if a%2==0:
            print("red")
        else:
            print("black")
            

            


