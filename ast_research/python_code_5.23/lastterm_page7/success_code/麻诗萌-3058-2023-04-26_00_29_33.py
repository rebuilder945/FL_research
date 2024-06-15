m=input()
dic={}
while (m!="q") :
    dic['m']=dic.get(m,0)+1
lst=[]
for k,v in dic.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1])
print(lst[-1][0],lst[-1][1])
