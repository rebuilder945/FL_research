pcolor1=input()
pcolor2=input()
lst=['red','blue','yellow']
if pcolor1==pcolor2:
    print('error')
elif pcolor1 not in lst or pcolor2 not in lst:
    print('error')
else:
    if {pcolor1,pcolor2}=={'red','blue'}:
        print('purple')
    if {pcolor1,pcolor2}=={'red','yellow'}:
        print('orange')
    if {pcolor1,pcolor2}=={'blue','yellow'}:
        print('green')

