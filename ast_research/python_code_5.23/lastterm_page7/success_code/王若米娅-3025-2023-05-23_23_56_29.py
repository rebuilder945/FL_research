ls=input().split(" ")
count_str={}
for  x in lst:
    count_str[x]=count_str.get(x,0)+1
ls=[]
for i in count_str:
    ls.append(count_str[i])
c=max(ls)
for i in coun_str:
    if count_str[i]==c:
        print(i,c)

