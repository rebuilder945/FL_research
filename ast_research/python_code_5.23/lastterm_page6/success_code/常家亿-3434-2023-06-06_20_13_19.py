a = input()
b = input()
lst = ['red','blue','yellow']
if a == b or a not in lst:
    print('error')
else:
    if a in ['red','blue'] and b in ['red','blue']:
        print('purple')
    elif a in ['red','yellow'] and b in ['red','yellow']:
        print('orange')
    elif a in['blue','yellow']and b in['blue','yellow']:
        print('green')
        




