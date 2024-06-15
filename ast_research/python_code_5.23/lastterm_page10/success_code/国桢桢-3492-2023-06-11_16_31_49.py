s = input()
l = []
if len(s)==0:
    print("None")
else:
    for i in s:
        if s.count(i)==1:
            l.append(i)
    print(l[0])
