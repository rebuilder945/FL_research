n=eval(input())
if type(n)!=type(1):
    print("error")
elif n<0 and n>36:
    print('error')
else:
    if n>0 and n<=10:
        if n%2==0:
            print("black")
        else:
            print("red")
    if n>=11 and n<=18:
        if n%2==0:
            print("red")
        else:
            print("black")
    if n>=19 and n<=28:
        if n%2==0:
            print("black")
        else:
            print("red")
    if n>=29 and n<=36:
        if n%2==0:
            print("red")
        else:
            print("black")
    if n==0:
        print("green")


