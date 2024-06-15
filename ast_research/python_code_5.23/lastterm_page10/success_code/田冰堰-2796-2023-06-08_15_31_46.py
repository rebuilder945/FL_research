s=input()
temp=[]
longest=[]
for i in range(len(s)):
    if '0'<=s[i]<='9':
        temp.append(s[i])
        if len(temp)>=len(longest):
            longest=temp.copy()
    else:
        temp=[]
if len(longest)>0:
    print("".join(longest))
else:
    print("No digits")
