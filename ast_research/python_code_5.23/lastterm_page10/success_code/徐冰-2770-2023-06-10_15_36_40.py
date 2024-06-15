def bianwei(a,b):
    for i in a:
        if i in b:
            b.remove(i)
        else:
            return False
    return True
a=list(input())
b=list(input())
if len(a)==len(b):
    print(bianwei(a,b))
else:
    print(False)

