
a=input()
b=input()
lsta=[]
lstb=[]
for x in a:
    lsta.append([a.count(x),x])
for x in b:
    lstb.append([b.count(x),x])
while True:
    for x in lsta:
        if x in lstb:
         pass
        else:
            print("False")
        break
    for x in lstb:
        if x in lsta:
         pass
        else:
            print("False")
        break
    print("True")
    break


