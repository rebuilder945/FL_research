n=eval(input())
if n in range(1,10,2):
    print('red')
elif n in range(2,11,2):
    print('black')
elif n in range(11,18,2):
    print('black')
elif n in range(20,29,2):
    print('black')
elif n in range(29,36,2):
    print('black')
elif n in range(12,19,2):
    print('red')
elif n in range(19,28,2):
    print('red')
elif n in range(30,37,2):
    print('red')
elif n==0:
    print('green')
else:
    print('error')
