a=str(input())
lst=[]
for i in  a:
    lst.append(i)
if lst==[]:
    print('None')
counts={}
for word in lst:
    counts[word]=counts.get(word,0)+1  
dic=list(counts.items())
for i in dic:
    if i[1]==1:
        print(i[0])
        break

