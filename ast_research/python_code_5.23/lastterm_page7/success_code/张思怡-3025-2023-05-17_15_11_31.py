a=input().split(" ")
dict={}
for x in a:
    dict[x]=dict.get(x,0)+1
list1=[]
list2=[]
for k,v in dict.items():
    list1.append([k,v])
list1.sort(key=lambda x:x[1],reverse=True)
m=1
for i in range(len(list1)-1):
    if list1[i][1]==list1[i+1][1]:
        m+=1
for i in range(m):
    list2.append([list1[i][0],list1[i][1]])

list2.sort()
for i in range(m):
    print(list2[i][0],list2[i][1])


