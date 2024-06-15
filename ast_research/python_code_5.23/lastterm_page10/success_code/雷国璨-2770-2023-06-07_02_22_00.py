a=list(input())
b=list(input())
if len(a)!=len(b):
    print('False')
else:
    if a.sort()==b.sort():
        print('True')
    else:
        print("False")
