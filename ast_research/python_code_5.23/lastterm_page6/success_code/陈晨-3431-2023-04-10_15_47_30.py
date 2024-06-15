n=eval(input())
if n not in range(0,37):
    print("error")
else:
    if n in range(1,11) or n in range(19,29):
        if n%2==0:
            print("black")
        else:
            print("red")
    elif n==0:
        print("green")
    else:
        if n%2==1:
            print("black")
        else:
            print("red")
            
