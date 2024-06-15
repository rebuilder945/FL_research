n=eval(input())
if n==0:
    print('green')
elif n in(1,11) or (19,29):
    if n%2:
        print('red')
    else:
        print('black')
elif n in(11,19) or(29,37):
    if n%2:
        print('black')
    else:
        print('red')

else:
    print('error')
