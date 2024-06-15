a=input()
b=input()
a1=len(a)
b1=len(b)
if a1==b1:
    for i in a:
        if i not in b:
            print('False')
            break
    for i in b:
        if i not in a:
            print('False')
            break
    else:
        print('True')
else:
    print('False')
