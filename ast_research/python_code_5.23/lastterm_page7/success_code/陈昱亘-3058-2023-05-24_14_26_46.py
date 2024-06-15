string=input() or 'q'
lst=[]
while string!='q':
    lst.append(string)
    string=input() or 'q'
dic={}
for x in lst:
    dic[x]=lst.count(x)
lst2=list(dic.items())
lst2.sort(key=lambda x:x[1],reverse=True)
Fstring,num=lst2[0]
print(Fstring,num)
