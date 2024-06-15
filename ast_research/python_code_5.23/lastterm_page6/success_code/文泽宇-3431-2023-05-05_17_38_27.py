n = int(input())
if n == 0:
    print('green')
elif n <= 10 and n%2 == 1:
    print('red')
elif n <= 10 and n%2 == 0:
    print('black')
elif n <= 18 and n%2 == 1:
    print('black')
elif n <= 18 and n%2 == 0:
    print('red')
elif n <= 28 and n%2 == 1:
    print('red')
elif n <= 28 and n%2 == 0:
    print('black')
elif n <= 36 and n%2 == 1:
    print('black')
elif n <= 36 and n%2 == 0:
    print('red') 
else:
    print('error')
