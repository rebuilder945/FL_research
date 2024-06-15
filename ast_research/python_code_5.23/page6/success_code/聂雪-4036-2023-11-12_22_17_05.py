a = eval(input())
if a>36 or a<0:
    print('error')
else:
    if a==0:
        print("green")
    elif a<=10:
        if a%2==0:
            print('black')
        else:
            print('red')
    elif a>=11 and a<=18:
        if a%2!=0:
            print('black')
        else:
            print('red')
    elif a>=19 and a<=28:
        if a%2==0:
            print('black')
        else:
            print('red')
    elif a>=29 and a<=36:
        if a%2!=0:
            print('black')
        else:
            print('red')
    
