a=input()
b=input()
x=[]
for i in a:
    if i in b:
        x.append(1)
    else:
        x.append(2)
if 2 in x:
    print("False")
else:
    print("True")
