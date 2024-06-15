a=input()
b=input()
ls=[]
if len(a)!=len(b):
    print("False")
else:
    for i in a:
        if i in b:
            ls.append(i)
if len(ls)==len(a):
    print("True")
else:
    print("False")
