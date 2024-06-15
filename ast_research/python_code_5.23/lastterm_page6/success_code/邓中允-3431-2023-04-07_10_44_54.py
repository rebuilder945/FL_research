n=eval(input())
if n>0 and n<11:
    if n%2==0:
            print("black")
    else:
            print("red")
elif n>10 and n<19:
    if n%2==0:
        print("red")
    else:
        print("black")
elif n>18 and n<29:
    if n%2==0:
        print("black")
    else:
        print("red")           
elif n>28 and n<37:
    if n%2==0:
        print("red")
    else:
        print("black") 
elif n==0:
        print("green")   

else:
    print("error")

