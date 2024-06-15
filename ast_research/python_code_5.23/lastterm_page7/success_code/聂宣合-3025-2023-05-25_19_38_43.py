s=input()
dic={}
for i in s.split(" "):
    dic[i]=dic.get(i,0)+1
maxvalue=max(dic.values())
for k,v in dic.items():
    if v == maxvalue:
        print(k,v)
