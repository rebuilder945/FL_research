m=input()
n=list(m)
lst=[]
s=''
for i in n:
    if i.isdigit():
        s=s+i
        if i == n[-1]:
            lst.append(s)
    else:
        lst.append(s)
        s=''
if m.isalpha():
    print("No digits")
else:
    lst.sort(key=len)
    print(lst[-1])


