from optparse import Values


dic={}
a=input().split('')
for x in a:
    if x not in dic.keys():
        dic[x]=1
    else:
        dic[x]+=1
for x in dic.keys():
    if dic[x]==max(dic.Values):
        print(x,dic[x])
