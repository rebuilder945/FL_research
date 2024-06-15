a=input() or "q"
dic={}
while a !="q":
    dic[a]=dic.get(a,0)+1
    a=input() or "q"
lst=list(dic.items())
lst.sort(key=lambda x :x[1],reverse=True)
print(lst[0][0],lst[0][1])

