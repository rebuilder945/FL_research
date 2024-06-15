dic={}
while True:
    n=input()
    if n!="q":
        dic[n]=dic.get(n,0)+1
    else:
        break 
lst=list(dic.items())   
lst.sort(key=lambda x:x[1], reverse=True)
print(lst[0][0],lst[0][1])
