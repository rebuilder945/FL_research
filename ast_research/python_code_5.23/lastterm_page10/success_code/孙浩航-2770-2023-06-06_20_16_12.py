def bianweisu(a,b):
    lisa=list(a)
    lisb=list(b)
    for x in lisa:
        if not x in lisb:
            return False
    return True
a=input()
b=input()
if len(a)!=len(b):
    print("Fales")
else:
    print(bianweisu(a,b))

