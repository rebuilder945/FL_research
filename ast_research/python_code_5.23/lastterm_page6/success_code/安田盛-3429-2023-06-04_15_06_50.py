s=input()
dic={}
dic["yin"]=0
dic[" "]=0
dic['shu']=0
dic["fu"]=0
for i in s:
    if "a"<=i<="z"or "A"<=i<="Z":
        dic["yin"]=dic.get('yin',0)+1
    elif i==" " :
        dic[" "]=dic.get(" ",0)+1
    elif "0"<=i<='9':
        dic['shu']=dic.get("shu",0)+1
    else:
        dic["fu"]=dic.get("fu",0)+1
lst=list(dic.values())
for x in lst:
    print(x,end=" ")





