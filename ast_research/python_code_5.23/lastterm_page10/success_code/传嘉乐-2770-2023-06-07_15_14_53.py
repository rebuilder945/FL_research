a=list(map(str,(input())))
b=list(map(str,(input())))
if len(a)==len(b):
    if a.sort()==b.sort():
        print('True')
    else:
        print('False')
else:
    print('False')



