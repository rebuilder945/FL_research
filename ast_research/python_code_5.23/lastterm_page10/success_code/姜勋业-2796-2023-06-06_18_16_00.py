s=input()
tmp=[]
longest=[]
for i in range(len(s)):
    if '0'<=s[i]<='9':
        tmp.append(s[i])
        if len(tmp)>=len(longest):
            longest=tmp.copy()
        else:
            tmp=[]
if len(longest)>0:
    print("".join(longest))
else:
    print("No digits")
