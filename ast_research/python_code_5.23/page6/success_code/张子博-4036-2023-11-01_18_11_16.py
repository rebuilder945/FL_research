a=int(input())
if a<0 or a>36:
    print("error")
if 0<a<11:
    if a%2==0:
        print("black")
    else:
        print("red")
if 10<a<19:
    if a%2==0:
        print("red")
    else:
        print("black")
if 18<a<29:
    if a%2==0:
        print("black")
    else:
        print("red")
if 30<a<37:
    if a%2==0:
        print("red")
    else:
        print("black")
if a==0:
    print("green")
