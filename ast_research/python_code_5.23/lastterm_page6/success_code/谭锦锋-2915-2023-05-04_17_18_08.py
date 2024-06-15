def f(number):
    a = number
    temp = 0
    while number !=0:
        temp += (number % 10)**3
        number = number // 10
    if a ==temp:
        print(a)
        return True
    
s = 0
c = int(input())
for x in range(2,c+1):
    if f(x):
        s = 1
if s == 0:
    print("none")

