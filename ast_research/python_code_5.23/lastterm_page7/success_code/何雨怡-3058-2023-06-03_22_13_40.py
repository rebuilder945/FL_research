string=input()
dic={}
while string!='q':
    dic[string]=dic.get(string,0)+1
    string=input()
diclist=[]
for k,v in dic.items():
    diclist.append([k,v])
diclist.sort(key=lambda x:x[1],reverse=True)
print(diclist[0][0],diclist[0][1])
