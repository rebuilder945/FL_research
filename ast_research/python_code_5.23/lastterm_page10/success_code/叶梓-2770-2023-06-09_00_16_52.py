a=input()
b=input()
lst1=list[a]
lst2=list[b]
if len(lst1)!=len(lst2):
    print("False")
if len(lst1)==len(lst2):
    for i in lst1:
        if i not in lst2:
            print("False")
    for x in lst2:
        if x not in lst1:
            print("False")
else:
    print("True")
