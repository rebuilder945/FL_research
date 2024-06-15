a=input()
b=input()
c=list(a)
d=list(b)
if len(c) == len(d):
    for i in c:
        if i in d:
            d.remove(i)
    if len(d) == 0:
        print('True')
else:
    print('False')    
