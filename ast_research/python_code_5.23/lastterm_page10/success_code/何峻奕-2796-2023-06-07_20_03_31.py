s=input()
tmp=[]
long=[]
for i in range(len(s)):
    if "0"<=s[i]<="9":
        tmp.append(s[i])
        if len(tmp)>=len(long):
            long=tmp.copy()
    else:
        tmp=[]
if len(long)>0:
    print("".join(long))
else:
    print("No digits")
