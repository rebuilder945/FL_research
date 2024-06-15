str=input()
dic={}
while str!='q':
    dic[str]=dic.get(str,0)+1
    str=input()
lst=list(dic.items())
lst.sort(key=lambda x:x[1],reverse=True)
a=lst[0][0]
b=lst[0][1]
print(a,b)


