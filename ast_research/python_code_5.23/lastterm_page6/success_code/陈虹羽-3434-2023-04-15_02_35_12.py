a=input()
b=input()
if a!="red" or a!='blue' or a!='yellow' or b!="red" or b!='blue' or b!='yellow':
    print('error')
if a==b:
    print('error')
else:
    if a=="red" and b=="blue":
        print('purple')
    if b=="red" and a=="blue":
        print('purple')
    if a=="red" and b=="yellow":
        print('orange')
    if b=="red" and a=="yellow":
        print('orange')
    if a=='blue' and b=="yellow":
        print('green')
    if b=='blue' and a=="yellow":
        print('green')
    
