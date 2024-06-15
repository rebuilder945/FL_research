a=input()
l=[]
longest=[]
for i in a:
    if 0<=i<=9:
        l.append(i)
        if len(l)>=len(longest):
            longest=l.copy()
    else:
        l=[]
if len(longest)>0:
    print("".join(longest))
else:
    print("No digits")
    

