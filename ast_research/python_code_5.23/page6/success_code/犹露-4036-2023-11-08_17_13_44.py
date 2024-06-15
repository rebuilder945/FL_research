koudai= eval(input())
if koudai==0:
    print("green")
if koudai in range(1,11):
    if koudai%2==0:
        print("black")
    else:
        print("red")
elif koudai in range(11,19):
    if koudai%2==0:
        print("red")
    else:
        print("black")
elif koudai in range(19,29):       
    if koudai%2==0:
            print("black")
    else:
            print("red")
elif koudai in range(29,37):
    if koudai%2==0:
        print("red")
    else:
        print("black")

if koudai>36 or koudai<0:
    print("error")

