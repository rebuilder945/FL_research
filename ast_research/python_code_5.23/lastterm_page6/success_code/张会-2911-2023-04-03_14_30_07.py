a = eval(input())
l = []
while a > 0:
    b = a % 10
    b += 5
    c = b%10
    l.append(c)
    a = int(a//10)
for i in range(len(l)):
    print(l[i], end='')
