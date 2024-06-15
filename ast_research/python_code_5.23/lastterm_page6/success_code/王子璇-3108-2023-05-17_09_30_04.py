s=input()
s.sort()
lst=[]
for x in s:
    for y in x:
        if y not in lst:
            print(s,s.count(y))
            lst.append(y)



