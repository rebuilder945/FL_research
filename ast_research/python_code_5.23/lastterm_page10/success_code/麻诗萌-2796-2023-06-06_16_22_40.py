n=list(input())
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
if lst==[]:
    print("No digits")
else:
    lst.sort(key=len)
    print(lst[-1])
print(lst)

