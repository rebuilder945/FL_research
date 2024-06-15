def bianwei(a,b):
    for i in a:
        if i in b:
            return True
        else:
            return False
a=list(input())
b=list(input())
if len(a)==len(b):
    print(bianwei(a,b))
else:
    print("False")

