def bianwei(a,b):
    for x in a:
        if x in b:
            b.remove(x)
        else:
            return False
    return True
a=list(input())
b=list(input())
if len(a)==len(b):
    print(bianwei(a,b))
else:
    print(False)

