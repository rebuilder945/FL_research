a = ' '
num = 0
sum = 0
while a != '#':
    a = input()
    if a != '#':
     sum += eval(a)
     num += 1
print('{} {}'.format(num,sum))
