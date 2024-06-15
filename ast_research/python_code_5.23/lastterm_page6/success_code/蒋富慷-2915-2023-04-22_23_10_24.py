a = eval(input())
d = 0
for x in range(2,a+1):
    b = 0
    c = x
    while x != 0:
        b += (x%10)**3
        x = x//10
    if b == c:
        d = 1
        print(c)
if d == 0:
    print('none')
