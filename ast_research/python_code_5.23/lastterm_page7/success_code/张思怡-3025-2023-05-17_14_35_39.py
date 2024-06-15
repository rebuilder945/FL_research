a=input().split(" ")
dict={}
for x in a:
    dict[x]=dict.get(x,0)+1
print(dict)
list1=[]
for k,v in dict.items():
    list1.append([k,v])
list1.sort(key=lambda x:x[1],reverse=True)
print(list1[0][0],list1[0][1])
