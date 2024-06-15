a=input()
b=input()
ls1=[x for x in a]
ls2=[y for y in b]
ls1.sort()
ls2.sort()
if ls1==ls2:
    print('True')
else:
    print('False')
