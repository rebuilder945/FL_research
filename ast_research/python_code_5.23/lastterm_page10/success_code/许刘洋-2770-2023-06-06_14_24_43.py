a=input()
b=input()
if len(a)==len(b) and (i for i in a) in b and (i for i in b) in a:
    print('True')
else:
    print('False')
