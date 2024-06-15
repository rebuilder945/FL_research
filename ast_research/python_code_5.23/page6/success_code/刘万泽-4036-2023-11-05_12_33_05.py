a=eval(input())
if a==0:
    print("green")
if 1<=a<=10:
    if a%2!=0:
        print("red")
    else:
        print("black")
if 11<=a<=18:
    if a%2!=0:
        print("black")
    else:
        print("red")
if 19<=a<=28:
    if a%2!=0:
        print("red")
    else:
        print("black")
if 29<=a<=36:
    if a%2!=0:
        print("black")
    else:
        print("red")
if a<0 or a>36:
    print("error")                        


