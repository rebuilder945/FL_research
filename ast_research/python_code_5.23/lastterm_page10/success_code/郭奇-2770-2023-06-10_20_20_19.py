a=input()
b=input()
if len(a)!=len(b):
    print('False')
else:
    ls1=list(a)
    ls2=list(b)
    lst1=sorted(ls1)
    lst2=sorted(ls2)
    if lst1==lst2:
        print('True')
    else:
        print('False')
