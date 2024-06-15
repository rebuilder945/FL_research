n=input()
dic={}
for x in n:
    dic[x]=dic.get(x,0)+1
lst=list(dic.items())
lst=[x for x in lst if x[1]==1]
if lst==[]:
    print("None")
else:
    print(lst[0][0])
