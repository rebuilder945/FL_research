a=input()
b=input()
lis1=[x for x in a]
lis2=[x for x in b]
lis1.sort()
lis2.sort()
if lis1==lis2:
    print("True")
else:
    print("False")

