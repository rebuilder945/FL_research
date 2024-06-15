strl=input() or 'q'
dic={}
while(strl!='q'):
    dic[strl]=dic.get(strl,0)+1
    strl = input() or 'q'
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse =True)
lst1=lst[0]
print(lst1[0],lst1[1])

