x=input()
d=[]
c=[]
for chars in x:
    if "0"<=chars<='9':
        d.append(chars)
        if len(d)>=len(c):
            c=d.copy()
    else:
        d=[]
if len(c)>0:
    print("".join(c))
else:
    print("No digits")


