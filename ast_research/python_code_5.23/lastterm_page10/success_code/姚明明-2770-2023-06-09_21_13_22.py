x=input()
y=input()
if len(x)!=len(y):
    print("False")
else:
    a=list(x)
    b=list(y)
    if a.sort()==b.sort():
        print("True")
    else:
        print("False")


