a=input()
b=input()
s=1
if len(a)!=len(b):
    print('False')
    s=0
else:
    for i in a:
        if i in b:
            continue
        else:
            s=0
            print('False')
            break
if s==1:
    print('True')
