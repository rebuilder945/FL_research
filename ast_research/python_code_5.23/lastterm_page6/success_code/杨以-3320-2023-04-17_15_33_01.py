length=eval(input())
width=(eval(input()))
if length<=0 or width<=0:
    print('illegal data')
else:
    if length==width:
        print('It\'s a square')
    elif length!=width :
        print('It\'s a rectangle')

