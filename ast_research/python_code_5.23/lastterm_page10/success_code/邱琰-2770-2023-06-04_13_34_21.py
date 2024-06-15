a=input()
b=input()
ls1=[i for i in a]
ls2=[i for i in b]
ls1.sorted()
ls2.sorted()
if ls1==ls2:
    print('True')
else:
    print('False')
