n=eval(input(""))
if n<0 or n>36:
    print("error")
elif n in range(1,11) and n%2==1:
    print("red")
elif n in range(1,11) and n%2==0:
    print("black")
elif n in range(11,19) and n%2==1:
    print("black")
elif n in range(11,19) and n%2==0:
    print("red")
elif n in range(19,29) and n%2==1:
    print("red")
elif n in range(19,29) and n%2==0:
    print("black")
elif n in range(29,37) and n%2==1:
    print("black")
elif n in range(29,37) and n%2==0:
    print("red")
else:
    print("green")            


