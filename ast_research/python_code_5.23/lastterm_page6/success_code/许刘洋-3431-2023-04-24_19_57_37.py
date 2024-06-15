a=eval(input())
if a==0:
    print("green")
if 1<=a<=10 or 19<=a<=28:
    if a%2==1:
        print("red")
    else:
        print("black")
if a>=11 and a<=18 or a<=29 and a>=36:
    if a%2==1:
        print("black")
    else:
        print("red")
if a<0 or a>36:
    print("error")

