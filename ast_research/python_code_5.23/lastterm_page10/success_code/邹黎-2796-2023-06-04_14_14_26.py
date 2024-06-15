a=input()
import copy
b=copy.deepcopy(a)
for x in a:
    if x not in list("0123456789"):
        a=a.replace(x," ")
if b!=a:
    lst=b.split()

    max=0
    for x in lst:
        if len(x)>=max:
            max=len(x)
    for x in reversed(lst):
        if len(x)==max:
            print(x)
            break
else:
    print("No digits")        
