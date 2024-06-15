a=eval(input())
m=0
if a in range(0,37):
    m=1
if m==0:
    print('error')
def even(x):
    if x%2==0:
        return 1
    else:
        return 0
if a in range(1,11):
    if even(a):
        print('black')
    else:
        print('red')
elif a in range(11,19):
    if even(a):
        print('red')
    else:
        print('black')
elif a in range(19,29):
    if even(a):
        print('black')
    else:
        print('red')
elif a in range(29,37):
    if even(a):
        print('red')
    else:
        print('black')
elif a==0:
    print('green')



