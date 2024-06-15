lst=input().split(' ')
dic={}
for x in lst:
    dic[x]=lst.count(x)
lst2=list(dic.items())
n=max(list(dic.values()))
str_list=[]
for a,b in lst2:
    if b==n:
        str_list.append(a)
str_list.sort()
for m in str_list:
    print(m,n)
