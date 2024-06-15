n=list(input())
b=[]
a=[]
for x in range(len(n)-1):
    if n[x].isdigit() and n[x+1].isdigit():
        b.append(n[x])
    elif n[x].isdigit() and n[x+1].isdigit()!=True:
        b.append(n[x]) 
        a.append(b)  
        b=[]
    elif n[x].isdigit() !=True:
        continue
c=0    
if a==[]:
    print("No digits")
else:
    a.sort(key=len)
    d=a[-1]
    for x in d:
        print(x,end='')
