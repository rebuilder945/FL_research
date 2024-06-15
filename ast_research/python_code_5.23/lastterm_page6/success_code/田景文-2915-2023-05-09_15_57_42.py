def flower(number):
    a = number
    b = 0
    while number != 0:
        b += (number % 10) ** 3
        number = number // 10
    if a == b:
        print(a)
        return True
    
flag = 0
number = int(input())
for i in range(2,number+1):
    if flower(i):
        flag = 1
if flag == 0:
    print("none")
