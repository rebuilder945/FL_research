item=input()or'q'
dic={}
while(item  !="q"):
    dic[item]=dic.get(item,0)+1
    item  =  input()  or  "q"
print(dic)
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
print(lst[0][0],end=' ')
print(lst[0][1])
