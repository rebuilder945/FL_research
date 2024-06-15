lst=eval(input())
jack=[]
for i in lst:
    if lst.count(i) ==1:
        jack.append(i)
    else:
        pass
jack.sort()
if len(jack)==0:
    print("False")
else:
    c=','.join(str(i) for i in jack)
    print(c)
