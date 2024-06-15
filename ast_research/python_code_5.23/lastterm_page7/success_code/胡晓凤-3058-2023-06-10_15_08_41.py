s=input()
dic={}
while s!="q":
    dic[s]=dic.get(s,0)+1
    s=input()
d1=sorted(list(dic.items()),key=lambda x:x[1],reverse=True)
print(d1[0][0],d1[0][1])
