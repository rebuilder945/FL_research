a=input()
b=input()
a1=list(a)
b1=list(b)
if len(a)==len(b):
    if a1.sort()==b1.sort():
        print("True")
    else:
        print("False")
else:
    print("False")
