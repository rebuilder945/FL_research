a=input()
b=input()
if len(a)!=len(b):
    print("False")
else:
    la=list(a)
    lb=list(b)
    la.sort()
    lb.sort()
    if la==lb:
        print("True")
    else:
        print("False")






