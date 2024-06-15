n=eval(input())
if n<0 or n>36:
    print("error")
else:
    if n==0:
        print(green)
    elif n>0 and n<11:
        if n%2==0:
            print(black)
        else:
            print(red)
    elif n>10 and n<19:
        if n%2==0:
            print(red)
        else:
            print(black)
    elif n>18 or n<29:
        if n%2==0:
            print(black)
        else:
            print(red)
    else:
        if n%2==0:
            print(red)
        else:
            print(black)
