n=eval(input())
if 0<n<11:
    if n%2!=0:
        print('red')
    else:
        print('black')
elif 10<n<19:
    if n%2!=0:
        print('black')
    else:
        print('red')
elif 18<n<29:
    if n%2!=0:
        print('red')
    else:
        print('black')
elif 28<n<37:
    if n%2!=0:
        print('black')
    else:
        print('red')
elif n==0:
    print("green")
else:
    print('error')
