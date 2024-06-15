a=input()
b=input()
if len(a)!=len(b):
    print("False")
else:
    for x in a:
        if x not in b:
            print("False")
            break
    else:
        print("True")
