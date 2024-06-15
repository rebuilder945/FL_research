a=list(input())
b=list(input())
ls=[]
for i in b:
    if i in a:
        ls.append(i)
if ls==b:
    print("True")
else:
    print("False")
