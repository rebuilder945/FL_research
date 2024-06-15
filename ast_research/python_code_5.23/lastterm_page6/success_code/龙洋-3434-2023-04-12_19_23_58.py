col1=input()
col2=input()
purple=['red','blue']
orange=['red','yellow']
green=['blue','yellow']
lis=['red','blue','yellow']
if col1 in lis and col2 in lis:
    if not col1==col2:
        if col1 in purple and col2 in purple:
            print('purple')
        elif col1 in orange and col2 in orange:
            print('orange')
        elif col1 in green and col2 in green:
            print('green')
    else:
        print("error")
else:
    print("error")
