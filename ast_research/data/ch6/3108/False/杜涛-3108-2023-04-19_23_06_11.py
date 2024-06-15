lst=eval(input())
dic={}
for i in lst:
    a=i[::]
    for x in a:
        dic[x]=dic.get(x,0)+1
list1=[]
for k,v in dic.items():
    list1.append([k,v])
list1.sort(key=lambda x:x[0],reverse=False)
print(list1)
for i in range(len(list1)):
    print("{},{}".format(list1[i][0],list1[i][1]))






