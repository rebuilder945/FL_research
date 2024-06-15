a=input()
b=input()
if len(a)!=len(b):
    print('False')
else:
    ls1=list(a)
    ls2=list(b)
    lst1=ls1.sort()
    lst2=ls2.sort()
    if lst1==lst2:
        print('True')
    else:
        print('False')
