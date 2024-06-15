n = eval(input())
if n <0 or n>36:
    print('error')
elif (1<= n <= 10 or 19<= n <= 28) and n%2 == 1:
    print('red')
elif (1<= n <= 10 or 19<= n <= 28) and n%2 == 0:
    print('black')
elif (11<= n <= 18 or 29<= n <= 36) and n%2 ==1:
    print('black')
elif (11<= n <= 18 or 29<= n <= 36) and n%2 == 0:
    print('red')
elif n == 0:
    print('green')

