n=eval(input())
if n==0:
    print("green")
elif 1<=n<=10 or 29<=n<=28:
    if n%2==1:
        print('red')
    else:
        print("black")
elif 11<=n<=18 or 29<=n<=36:
    if n%2==1:
        print("black")
    else:
        print("red")
elif n<0 or n>36:
    print("error")
