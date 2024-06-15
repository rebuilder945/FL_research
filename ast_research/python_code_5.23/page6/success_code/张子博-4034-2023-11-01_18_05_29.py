a=input()
b=input()
if a==b or a not in ['red','yellow','blue'] or b not in ['red','yellow','blue']:
    print("error")
if (a=='red'and b=="blue") or (b=='red'and a=="blue"):
    print("purple")
if (a=='red'and b=="yellow") or (b=='red'and a=="yellow"):
    print('orange')
if (a=='blue'and b=="yellow") or (b=='blue'and a=="yellow"):
    print('green')

