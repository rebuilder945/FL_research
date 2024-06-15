s=list(input())
dengji=0
if len(s)>=8:
    dengji+=1
n=[]
xiaoxie=[]
daxie=[]
qiguai=[]
for i in s:
    if ord('a')<=ord(i)<=ord('z'):
        xiaoxie.append(i)
    elif ord('A')<=ord(i)<=ord('Z'):
        daxie.append(i)
    elif i.isdigit():
        n.append(i)
    else:
        qiguai.append(i)
if n:
    dengji+=1
if xiaoxie:
    dengji+=1
if daxie:
    dengji+=1
if qiguai:
    dengji+=1
print(dengji)
