s=input()
a=[]
k=''
s+=' '
for x in range(len((s))-1):
    if '0'<=s[x]<='9':
        k+=s[x]
    if len(k)>0 and (s[x+1]<'0'or s[x+1]>'9'):
        a.append(k)
        k=''
b=''
if len(a)==0:
    print("No digits")
else:
    for x in a:
        if len(x)>=len(b):
            b=x
print(b)
