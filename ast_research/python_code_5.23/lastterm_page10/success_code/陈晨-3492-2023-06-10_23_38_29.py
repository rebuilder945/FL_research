s=input() or None
if s==None:
    print("None")
else:
    ls=[]
    for i in s:
        if s.count(i)==1:
            ls.append(i)
    print(ls[0])
               

