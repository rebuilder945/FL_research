a=input()
b=input()
c=['red','blue','yellow']
if a==b or a not in c or b not in c:
    print('error')
else:
    if (a or b =='red')and (a or b =='blue'):
        print('purple')
    elif (a or b =='red')and (a or b =='yellow'):
        print('orange')
    elif (a or b =='blue')and (a or b =='yellow'):
        print('green')
