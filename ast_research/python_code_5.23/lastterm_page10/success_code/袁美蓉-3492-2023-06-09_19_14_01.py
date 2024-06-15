s = input()
if len(s)>0:
    ls = []
    for i in range(0,len(s),1):
        if s.count(s[i])==1:
            ls.append(s[i])
    print(ls[0])
elif len(s)==0:
    print('none')

