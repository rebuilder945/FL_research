c1=input()
c2=input()
lst=['red','blue','yellow']
if c1 not in lst or c2 not in lst or c1==c2:
    print('error')
elif c1 in lst[0:2] and c2 in lst[0:2]:
    print('purple')
elif c1 in lst[0:3:2] and c2 in lst[0:3:2]:
    print('orange')
else:
    print('green')
