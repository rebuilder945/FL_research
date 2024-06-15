a=input()
b=input()
ls1=[i for i in a]
ls2=[i for i in b]
ls1.sort()
ls2.sort()
if ls1==ls2:
    print('True')
else:
    print('False')
