s=input()
s.sort()
lst=[]
for x in s:
    if x not in lst:
        print(s,s.count(x))
        lst.append(x)



