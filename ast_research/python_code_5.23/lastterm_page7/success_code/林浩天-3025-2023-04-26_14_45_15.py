a=input()
b=a.split()
word={}
c=[]  
for i in b:
    if i in c:
        word[i]+=1
    else:
        c.append(i)
        word[i]=1
d=max(word.values())
e=[]
for i in word:
    if word[i]==d:
        e.append(i)
f=sorted(e)
for i in f:
    print(i,d)

