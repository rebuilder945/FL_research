n = eval(input())

if n<0 or n>36:
    print('error')
elif n == 0:
    print('green')
elif (n>=1 and n<=10) or (n>=19 and n<=28):
    if n%2 == 1:
        print('red')
    elif n%2 == 0:
        print('black')
elif (n>=11 and n<=18) or (n>=29 and n<=36):
    if n%2 == 0:
        print('red')
    else:
        print('black')
