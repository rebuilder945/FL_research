str,cnt="None",0
dic={}
s=input()
while s!="q":
    dic[s]=dic.get(s,0)+1
    s=input()
for k,v in dic.items():
    if v>cnt:
        str,cnt=k,v
print(str,cnt)
