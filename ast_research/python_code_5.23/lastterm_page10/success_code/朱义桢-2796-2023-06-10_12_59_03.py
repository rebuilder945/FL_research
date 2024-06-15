a=input()
b=[]
for i in range(1,len(a)+1):
    for x in range(i+1,len(a)+2):
        if a[i-1:x-1].isdigit():
            b.append(a[i-1:x-1])
max=0
c=[]
for x in b:
    if x.isdigit() and len(x)>=max:
        c.append(x)
        max=len(x)
if c==[]:
    print("No digits")
else:
    c.sort(reverse=True)
    c.sort(key=len,reverse=True)
    print(c[0])       
