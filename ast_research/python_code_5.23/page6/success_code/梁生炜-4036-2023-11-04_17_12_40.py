n=eval(input())
if n in range(1,10,2) or (19,28,2) or (12,19,2) or (30,37,2):
    print('red')
elif n in range(2,11,2) or (20,27,2) or (11,18,2) or (29,36,2):
    print('black')
elif n==0:
    print('green')
else:
    print('error')
