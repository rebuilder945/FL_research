n=eval(input())
if n==0:
    print("green")
elif 1<=n<=10 or 19<=n<28:
    if n%2==1:
        print("red")
    else:
        print("black")
elif 11<=n<=28 or 29<=n<36:
    if n%2==1:
         print("black")
    else:
        print("red")
else:
    print("error")

