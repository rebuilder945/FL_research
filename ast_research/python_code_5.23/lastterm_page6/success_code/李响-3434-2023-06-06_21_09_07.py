a = input()
b = input()
c = {a,b}
d1 = {'red','yellow'}
d2 = {'red','blue'}
d3 = {'blue','yellow'}
if c == d2:
    print('purple')
elif c == d3:
    print('green')
elif c == d1:
    print('orange')
elif a == b:
    print('error')
else:
    print('error')
