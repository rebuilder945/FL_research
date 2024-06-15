a=input().split()
b=input().split()
for x in a:
    if x in b and a.index(x)!=b.index(x):
        print('True')
    else:
        print('False')

