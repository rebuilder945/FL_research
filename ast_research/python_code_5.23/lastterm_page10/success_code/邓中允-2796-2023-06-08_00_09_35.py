s=list(input())
a=[]
for i in range(len(s)):
    if s[i-1].isalpha and s[i].isdigit:
        a.append(s[i])
    elif s[i].isdigit and s[i+1].isdigit:
        a.append(s[i])
    elif s[i].isdigit and s[i+1].isalpha:
        a.append(s[i])
        a.append(',')
a.sort()
if len(a)==0:
    print("No digits")
else:
    print(a[0])


