num=eval(input())
if type(num)==int and num in range(37):
    if num in range(1,11):
        if num%2==0:
            print("black")
        else:
            print("red")
    elif num in range(11,19):
        if num%2==0:
            print("red")
        else:
            print("black")
    elif num in range(19,29):
        if num%2==0:
            print("black")
        else:
            print("red")
    elif num in range(29,36):
        if num%2==0:
            print("red")
        else:
            print("black")
    else:
        print("green")
else:
    print("error")
