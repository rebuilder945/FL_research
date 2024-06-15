s = input()
if len(s)==0:
    print("None")
else:
    for i in range(0,len(s),1):
        list = []
        if s.count(s[i])==1:
            list.append(s[i])
    print(list[0])

