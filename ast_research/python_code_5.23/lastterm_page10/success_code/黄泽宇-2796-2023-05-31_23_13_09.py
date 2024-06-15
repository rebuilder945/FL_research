s = "sdffsd123werrer456fgdgdg1dfgdf12"
s=list(s)
lan=[]
b=0
hi=""
for i in range(len(s)):
    x=ord(s[i])
    if x in range(48,58):
        hi += s[i]
        b+=1
    elif x not in range(48,58) and hi != "":
        lan.append(hi)
        hi=""
        b=0
if b!=0:
    lan.append(hi)
if lan == []:
    print("No digits")
else:
    lan.sort(key=len)
    print(lan[-1])

