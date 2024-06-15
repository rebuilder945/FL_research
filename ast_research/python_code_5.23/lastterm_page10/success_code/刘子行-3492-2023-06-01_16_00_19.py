ass=input()
if len(ass)==0:
    print('None')
else:
    hole=[]
    for x in ass:
        if ass.count(x)==1:
            hole.append(x)
    print(hole[0])

