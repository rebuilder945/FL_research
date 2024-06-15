a = input()
b = input()
c = ['red','blue','yellow']
def mix(a,b):
    if a in ['red','blue'] and b in ['red','blue']:
        print('purple')
    elif a in ['red','yellow'] and b in ['red','yellow']:
        print('orange')
    else:
        print('green')
if a == b or a not in c or b not in c:
    print('error')
else:
    mix(a,b)
