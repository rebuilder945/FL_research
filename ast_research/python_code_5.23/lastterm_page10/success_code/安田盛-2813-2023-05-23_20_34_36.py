s=input()
a=input()
if s.count(a)==0:
    print(s)
else:
    for i in s:
        if i==a:
            aa=s.replace(i,"")
    print(aa)
