a = input()
b = input()
if len(a)!=len(b):
    print('False')
else:
    n=0
    for x in a:
        if x not in b or a.count(x)!=b.count(x):
            print('False')
            n=1
        break
    if n==0:
        print('True')

