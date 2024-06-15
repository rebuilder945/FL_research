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
for i in word:
    if word[i]==d:
        print(i,d)

