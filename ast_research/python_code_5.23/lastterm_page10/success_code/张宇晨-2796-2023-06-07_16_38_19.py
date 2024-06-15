a=input()
b=[]
longest=[]
for x in a:
    if x.isdigital():
        b.append(x)
        if len(b)>len(longest):
            longest=b.copy()
    else:
        b=[]
if len(longest)==0:
    print("No digits")
