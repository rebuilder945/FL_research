word = input() or "q"
dic={}
while word!="q":
    dic[word]=dic.get(word,0)+1
    word = input() or "q"
lst=[]
for k,v in dic:
    lst.append([k,v])
lst.sort(lambda x:x[1],reverse=True)
print(lst[0][0],lst[0][1])

