a=input()
b=[]
longest=[]
for x in a:
    if "0"<=x<="9":
        b.append(x)
        if len(b)>=len(longest):
            longest=b.copy()
    else:
        b=[]
    
if len(longest)==0:
    print("No digits")
else:
    print("".join(longest))
