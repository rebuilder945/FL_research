m=eval(input())
if m>36 or m<0:
    print('error')
elif 1<=m<=10 or 19<=m<=28:
    if m%2==0:
        print("black")
    else:
        print('red')
elif 11<=m<=18 or 29<=m<=36:
    if m%2==0:
        print("red")
    else:
        print('black')
elif m==0:
    print('green')
