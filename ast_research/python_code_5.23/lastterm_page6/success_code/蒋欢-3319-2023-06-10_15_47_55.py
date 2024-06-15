def check(m,n):
    if m>=99 and n>=99:
        print('You won a scholarship of 500 yuan!')
    elif m<30 or n<30:
        print('You need to relearn!')
m=eval(input())
n=eval(input())
check(m,n)
