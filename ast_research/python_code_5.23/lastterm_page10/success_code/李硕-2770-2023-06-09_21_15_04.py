a=eval(input())
b=eval(input())
if len(a)!=len(b):
    print("False")
else:
    if sorted(a)==sorted(b):
        print("True")
    else:
        print("False")

