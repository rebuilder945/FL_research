s=list(str(input()))
if s==[]:
    print("None")
elif s!=[]:
    l=[]
    for i in s:
        if s.count(i)==1:
            l.append(i)
    print(l[0])
