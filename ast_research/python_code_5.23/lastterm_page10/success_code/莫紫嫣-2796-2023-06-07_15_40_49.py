s=input()
a=[]
b=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        a.append(s[i])
        if len(a)>=len(b):
            b=a.copy()
    else:
        a=[]
if len(b)>0:
    print("".join(b))
else:
    print("No digits")
