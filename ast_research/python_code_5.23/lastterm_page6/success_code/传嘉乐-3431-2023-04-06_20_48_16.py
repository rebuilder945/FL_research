a=int(input())
if a==0:
    print('green')
elif (0<a<11 or 18<a<29) and a%2!=0:
    print('red')
elif (0<a<11 or 18<a<29) and a%2==0:
    print('black')
elif (10<a<19 or 28<a<37) and a%2!=0:
    print('black')
elif (10<a<19 or 28<a<37) and a%2==0:
    print('red')
else:
    print('error')

