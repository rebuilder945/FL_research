a=input()
b=a.split()
word={}
c=[]
for i in b:
    m=0
    if i in c:
        m+=1
        word[i]=m
    else:
        c.append(i)
        m+=1
        word[i]=m
d=max(word.values())
for i in word:
    if word[i]==d:
        print(i,d)

