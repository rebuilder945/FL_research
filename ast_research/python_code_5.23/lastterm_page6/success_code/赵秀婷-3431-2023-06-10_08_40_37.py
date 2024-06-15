#     print('error')

n=eval(input())
if n in range(1,11,2) or n in range(12,19,2) or n in range(19,28,2) or n in range(30,37,2):
    print('red')
if n not in range(0,37):
    print('error')
else:
    print('black')
