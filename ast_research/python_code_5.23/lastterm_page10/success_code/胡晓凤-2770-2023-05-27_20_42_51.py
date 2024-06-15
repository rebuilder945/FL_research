a=input()
b=input()
ls1=[]
ls2=[]
for i in a:
    ls1.append(i)
for j in b:
    ls2.append(j)
ls1.sort()
ls2.sort()
if ls1==ls2:
    print("True")
else:
    print("False")
