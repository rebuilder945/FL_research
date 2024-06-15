import re
istr=str(input())
ilist=re.split("(\d+)",istr)
a=1
if len(ilist)==1 and ilist[0].isalpha():
    print("No digits")
else:
    for x in ilist:
        if x.isdigit():
            if len(x)>=a:
                a=len(x)
                m=x
    print(m)





