number=eval(input())
if number>36 or number<0:
    print("error")
else:
    if number==0:
        print("green")
    elif 11>number>0:
        print("black")
    elif 19>number>10:
        print("red")
    elif 29>number>18:
        print("black")
    elif 37>number>28:
        print("red")
