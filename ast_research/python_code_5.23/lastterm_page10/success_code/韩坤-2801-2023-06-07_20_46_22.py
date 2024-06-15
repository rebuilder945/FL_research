n=input()
i=0
lst=["~","!","@","#","$","%","^","&","*","()","_","=","-","/",",",".","?","<",">",";",":","[]","{}","|","\\"]
if len(n)>=8:
    i+=1
dic={}
for x in n:
    if x.isupper():
        dic[3]=dic.get(3,0)+1
        continue
    if x.islower():
        dic[2]=dic.get(2,0)+1
        continue
    if x in lst:
        dic[5]=dic.get(5,0)+1
        continue
    if x.isdigit():
        dic[1]=dic.get(1,0)+1
        continue
lst2=list(dic.items())
for x in lst2:
    if x[1]>0:
        i+=1
print(i)

