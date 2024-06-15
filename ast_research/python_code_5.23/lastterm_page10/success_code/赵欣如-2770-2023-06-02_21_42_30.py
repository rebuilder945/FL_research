a=list(input())
b=list(input())
if len(a)==len(b):
    for x in a:
        if x in b:
            b.remove(x)
    if len(b)==0:
        print("True")
else:
    print("False")

