a=list(input())
b=list(input())
la=len(a)
lb=len(b)
sa=set(a)
sb=set(b)
if la!=lb:
    print("False")
else:
    if sa==sb:
        print("True")
    else:
        print("False")

            

