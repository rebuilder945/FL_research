def flower(number):
    n = number
    x = 0
    while number != 0:
        x += (number % 10) ** 3
        number = number // 10
    if n == x:
        print(n)
        return True
t = 0
number = int(input())
for i in range(2,number+1):
    if flower(i):
        t = 1
if t == 0:
    print('none')
