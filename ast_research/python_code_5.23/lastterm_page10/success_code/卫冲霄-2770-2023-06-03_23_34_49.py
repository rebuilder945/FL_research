a=input()
b=input()
if len(a)!=len(b):
    print("False")
else:
    a.sort()
    b.sort()
    if a==b:
        print("True")
    else:
        print("False")
