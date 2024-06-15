str=input()
dic={}
while str!='q':
    dic[str]=dic.get(str,0)+1
    str=input()
lst=[]
for k,v,in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
string1=lst[0][0]
string2=lst[0][1]
print(string1,string2)
