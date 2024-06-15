a=input().split()
b=input().split()
for x in a:
    if x in b and a.index(x)!=b.index(x) and len(a)==len(b):
        print('True')
    else:
        print('False')

