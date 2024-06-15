a=list(input())
b=list(input())
if len(a)==len(b):
    for i in range(len(a)):
        if a[i] in b:
            print('True')
        else:
            print('False')
else:
    print('False')
