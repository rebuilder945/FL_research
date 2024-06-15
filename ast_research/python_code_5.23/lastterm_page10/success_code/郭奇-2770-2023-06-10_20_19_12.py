a=input()
b=input()
if len(a)!=len(b):
    print('False')
else:
    ls1=list(a)
    ls2=list(b)
    ls1.sorted()
    ls2.sorted()
    if ls1==ls2:
        print('True')
    else:
        print('False')
