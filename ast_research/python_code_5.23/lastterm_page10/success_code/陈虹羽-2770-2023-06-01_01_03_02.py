a=input()
b=input()
a1=len(a)
b1=len(b)
c=0
if a1==b1:
    for i in a:
        if i not in b:
           c=-1
            
    for i in b:
        if i not in a:
            c=-1

    if c==0:
        print('True')
    else:
        print('False')

else:
    print('False')
