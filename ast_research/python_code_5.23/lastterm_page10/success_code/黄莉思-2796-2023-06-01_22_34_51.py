a=list(input())
b=[]
c=[]
jishu=0
long=len(a)
while 1:
    if jishu==long-1:
        if a[jishu].isdigit():
            b.append(a[jishu])
            c.append(b)
            b=[]
        break
    elif a[jishu].isdigit() and a[jishu+1].isdigit():
        b.append(a[jishu])
    elif a[jishu].isdigit() and a[jishu+1].isdigit()!=True:
        b.append(a[jishu])
        c.append(b)
        b=[]
    jishu+=1
jishu=0
for i in c:
    if len(i)>jishu:
        jishu=len(i)
lst1=[]
for i in c:
    if len(i)==jishu:
        lst1=i
if len(lst1)!=0:
    for i in lst1:
        print(i,end="")
else:
    print("No digits")
    
