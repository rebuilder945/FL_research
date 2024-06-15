Num = eval(input())
if Num == 0:
    print("green")
elif 0<=Num<=10:
    print("red") if Num%2==1 else print("black")
elif Num<=18:
    print("black") if Num%2 ==1 else print("red")
elif Num<=28:
    print("red") if Num%2==1 else print("black")
elif Num<=36:
    print("black") if Num%2 ==1 else print("red")
else:
    print("error")
