a=list(map(str,(input())))
b=list(map(str,(input())))
a.sort()
b.sort()
c=0
if len(a)==len(b):
    for x in range(len(a)):
        if a[x]==b[x]:
            c+=1
if c==len(a):
        print('True')
else:
        print('False')
