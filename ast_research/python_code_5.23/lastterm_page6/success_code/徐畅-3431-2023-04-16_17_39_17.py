n=int(eval(input()))
if n>=0 and n<=36:
    if n in range(1,11):
        if n%2==1:
                 print("red")
        else:
                 print("black")
    elif n in range(11,19):
        if n%2==1:
              print("black")
        else:
         print("red")
    elif n in range(19,29):
        if n%2==1:
             print("red")
        else:
             print("black")
    elif n in range(29,37):
        if n%2==1:
              print("black")
        else :
             print("red")
    elif n==0:
         print("green")

else:
    print("error")
