a=int(input())
list1={i for i in range(0,37) }
if not a in list1:
    print("error")
elif a==0:
    print("green")
elif 0<a<=10:
    if a%2==0:
        print("black")
    elif a%2==1:
        print("red")
elif 10<a<=18:
    if a%2==0:
        print("red")
    elif a%2==1:
        print("black")
elif 18<a<=28:
    if a%2==0:
        print("black")
    elif a%2==1:
        print("red")
elif 28<a<=36:
    if a%2==0:
        print("red")
    elif a%2==1:
        print("black")            
