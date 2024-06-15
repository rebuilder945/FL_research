stext=input()
a1=[]
a2=[]
if stext!="":
    for s in stext:
        a1.append(s)
    for i in stext:
        if a1.count(i)==1:
            a2.append(i)
    for j in stext:
        if j in a2:
            print(j)
            break
else:
    print("None")
