c1=input()
c2=input()
s1={c1,c2}
purplel={'red','blue'}
orangel={'red','yellow'}
greenl={'blue','yellow'}
allc={'red','blue','yellow'}
if c1 not in allc or c2 not in allc or c1==c2:
    print('error')
elif s1==purplel:
    print('purple')
elif s1==orangel:
    print('orange')
else:
    print('green') 
