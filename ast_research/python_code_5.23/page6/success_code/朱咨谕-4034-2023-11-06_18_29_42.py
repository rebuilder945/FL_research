c1=input()
c2=input()
#red blue yellow
#if c1=='red':print(1)
if c1==c2 or (c1!='red' and c1!='yellow' and c1!='blue') or (c2!='red' and c2!='yellow' and c2!='blue') :
    print('error')
else:
    if c1=='red':
        if c2=='blue':
            print('purple')
        else:
            print('orange')
    elif c1=='blue':
        if c2=='red':
            print('purple')
        else:
            print('green')
    else :
        if c2=='red':
            print('orange')
        else:
            print('green')
