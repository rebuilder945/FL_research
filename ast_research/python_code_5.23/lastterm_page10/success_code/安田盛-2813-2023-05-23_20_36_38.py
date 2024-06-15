s=input()
a=input()
if s.count(a)==0:
    print(s)
else:
    new=s.replace(a,"")
    print(new)
