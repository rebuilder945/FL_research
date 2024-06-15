n=eval(input())
m=eval(input())
if n<0 or m<0:
    print('illegal date')
elif m==n:
    print('It\'s a square')
else:
    print('It\'s a rectangle')
