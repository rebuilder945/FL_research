a=input()
b=input()
i=0
if len(a)!=len(b):
    print('False')
else:
    for x in a:
        if b.find(x)!=-1:
            i=i+1
        else:
            i=i-1
    if i==len(a):
        print('True')
    else:
        print('False')
