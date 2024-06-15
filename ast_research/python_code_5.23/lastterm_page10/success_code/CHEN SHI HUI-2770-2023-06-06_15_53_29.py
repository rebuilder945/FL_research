a=list(input())
b=list(input())
a.sort()
b.sort()
if len(a)==len(b):
    if a==b:
        print('True')
    else:
        print('False')
else:
    print('False')
