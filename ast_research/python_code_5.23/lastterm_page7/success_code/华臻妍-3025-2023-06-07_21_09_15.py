s=input().split(' ')
dic={}
dic['name']=s[0]
dic['english']=eval(s[1])
dic['python']=eval(s[2])
dic['math']=eval(s[3])
dic['avg']=(dic['english']+dic['python']+dic['math'])/3
print(dic['name'],end=' ')
lst=list(dic.values())
lst1=[x for x in lst[1:4]]
lst2=list(map(int,lst1))
lst2.sort(reverse=True)
for x in lst2:
    print("%.2f"%(x),end=' ')
print("%.2f"%(dic['avg']))
