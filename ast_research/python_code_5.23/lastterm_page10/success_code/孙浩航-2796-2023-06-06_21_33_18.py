s=input()
a=[]
b=[]
for x in range(len(s)):
    if "0"<=s[x]<="9":
        a.append(s[x])
        if len(a)>=len(b):
            b=a.copy()
    else:
        a=[]
if len(b)>0:
    print("".join(b))
else:
    print("No digits")

