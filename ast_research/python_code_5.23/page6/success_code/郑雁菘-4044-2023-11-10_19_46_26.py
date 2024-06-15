def flower(n):
    a = n
    b = 0
    while n != 0:
        b += (n % 10)**3
        n = n // 10
    if a == b:
        print(a)
        return True
M = 0
number = int(input())
for i in range(2,number + 1):
    if flower(i):
        M = 1
if M == 0:
    print("none")
