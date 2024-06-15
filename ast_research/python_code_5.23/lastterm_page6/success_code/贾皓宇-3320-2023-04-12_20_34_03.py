a=eval(input())
b=eval(input())
if int(a)<=0 or int(b)<=0:
    print('illegal data')
else:
    if a==b:
        print('It\'s a square')
    else:
        print('It\'s a rectangle')
