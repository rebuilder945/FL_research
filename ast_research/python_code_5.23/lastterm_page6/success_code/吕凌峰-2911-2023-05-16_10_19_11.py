def encryption(x):
    Sum = []
    while x > 0:
        Sum.append((x % 10 + 5) % 10)
        x = x // 10
    for i in Sum:
        print(i, end='')
num = int(input())
encryption(num)
