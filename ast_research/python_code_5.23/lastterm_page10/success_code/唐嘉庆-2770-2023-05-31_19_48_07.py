a=input()
b=input()
lst=[]
lst1=[]
for i in a:
    lst.append(i)
for i in b:
    lst1.append(i)
count={}
for word in lst:
    count[word]=count.get(word,0)+1  
count1={}
for word in lst1:
    count1[word]=count1.get(word,0)+1  
dic=list(count.keys())
dic1=list(count1.keys())
dic.sort()
dic1.sort()
dics=list(count.values())
dics1=list(count1.values())
dics.sort()
dics1.sort()
if dic==dic1 and dics==dics1:
    print('True')
else:
    print('False')


