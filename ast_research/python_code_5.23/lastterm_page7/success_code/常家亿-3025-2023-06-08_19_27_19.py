a=input()
b =a.split()
dic ={}
for x in b:
    if x not in dic:
        dic[x]=1
    elif x in dic:
        dic[x]+=1
lst = list(dic.values())
c = max(lst)
lst1 =[]
for s in dic:
    if dic[s]==c:
        lst1.append(s)
lst1.sort()
for t in lst1:
    print(t,c)

        



