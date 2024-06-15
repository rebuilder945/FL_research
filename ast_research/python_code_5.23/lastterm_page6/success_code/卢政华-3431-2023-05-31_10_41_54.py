num=eval(input())
if 1<=num<=10 or 19<=num<=28:
    for i in range(num):
        if i%2==0:
            print("black")
        else:
            print("red")
elif 11<=num<=18 or 29<=num<=36:
    for i in range (num):
        if i%2==0:
            print("red")
        else:
            print("black")
elif num==0:
    print("green") 
else:
    print("error")
