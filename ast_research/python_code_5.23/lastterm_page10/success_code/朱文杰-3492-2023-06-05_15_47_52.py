str=input()
i="None"
if str!="None":
    ls=[]
    for s in str:
        if str.count(s)==1:
            ls.append(s)
            i=ls[0]
print(i)
