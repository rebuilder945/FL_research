def cal(x):
    if eval(x)<20:
        t=6*(eval(x)**2)+1
        print('%.2f'%t)
    elif 20<=eval(x)<40:
        t=(3*eval(x)-60)**0.5
        print('%.2f'%t)
    else:
        t=100/(eval(x)+1)
        print('%.2f'%t)
n=input()
cal(n)
