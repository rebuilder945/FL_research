na=input().split()
summ={}
for word in na:
    if word in summ:
        summ[word]+=1
    else:
        summ[word]=1
big=max(summ.values())

lis=[]
for word,c in summ.items():
    if c==big:
        lis.append(word)
lis.sort()
for word in lis:
    print(word,big)
