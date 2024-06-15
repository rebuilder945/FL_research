x=input()
y=input()
if len(x)!=len(y):
    print("False")
else:
    if x.sort()==y.sort():
        print("True")
    else:
        print("False")


