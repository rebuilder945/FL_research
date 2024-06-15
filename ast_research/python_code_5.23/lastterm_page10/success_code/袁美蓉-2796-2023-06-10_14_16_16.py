s = input()
if type(s)==str:
    print('No dijits')
else:
    for a in s:
        if type(a)==str:
            s.replace(a,'')
    ls = s.split()
    for i in ls:
        if type(i)==int:
            print(max(i))
