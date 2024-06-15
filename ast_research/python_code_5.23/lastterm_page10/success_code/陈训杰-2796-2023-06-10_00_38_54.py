s=input()
m=""
for i in s:
    if i.isdigit():
        m+=i
    else:
        m+="-"
m=m.split('-')
n=[]
for i in m:
    if i.isdigit():
        n.append(i)
if n==[]:
    print("No digits")
else:
    a=[]
    for i in n:
        a.append(len(i))
    for i in range(-1,-len(n)-1,-1):
        if len(n[i])==max(a):
            print(n[i])
            break
