lst=input().split()
dic={}
for i in lst:
    dic[i]=dic.get(i,0)+1
list=[]
for k,v in dic.items():
    list.append([k,v])
list.sort(key=lambda x:x[1],reverse=True)
list.sort(key=lambda x:x[0])

for i in range(len(list)):
    if i<len(list):
        while list[i][1]==list[0][1]:
            print('%s %d'%(list[i][0],list[i][1]))
            break
