n=list(input())
lst=[]
s=''
for i in n:
    if i.isdigit():
        s=s+i
    else:
        lst.append(s)
        s=''
if len(lst)==0:
    print("No digits")
else:
    lst.sort(key=len)
    print(lst[-1])


