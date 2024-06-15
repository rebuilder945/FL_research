def bw(s1,s2):
    l1=str(s1)
    l2=str(s2)
    if len(l1)!=len(l2):
        return "False"
    else:
        b1=[x for x in l1]
        b2=[y for y in l2]
        o1=b1.copy()
        o2=b2.copy()
        for i in b1:
            a=l2.find(i)
            if a == -1:
                return "False"
            else:                
                o1.remove(i)
                o2.remove(i)
                if len(o1) == 0:
                    return "True"
d=input()
v=input()
print(bw(d,v))

