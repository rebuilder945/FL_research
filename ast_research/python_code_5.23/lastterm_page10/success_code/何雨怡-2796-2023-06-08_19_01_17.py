s=input()
tem=[]
longest=[]
for i in range(len(s)):
    if '0'<=s[i]<='9':
        tem.append(s[i])
        if len(tem)>=len(longest):
            longest=tem.copy()
        else:
            tmp=[]
if len(longest)>0:
    print(''.join(longest))
else:
    print('No digits')
