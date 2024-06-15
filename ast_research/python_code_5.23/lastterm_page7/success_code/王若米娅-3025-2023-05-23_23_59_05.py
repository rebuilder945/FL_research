ls=input().split(" ")
ls.sort()
count_str={}
for  x in ls:
    count_str[x]=count_str.get(x,0)+1
lst=[]
for i in count_str:
    lst.append(count_str[i])
c=max(lst)
for i in count_str:
    if count_str[i]==c:
        print(i,c)

