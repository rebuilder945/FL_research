a=input().split()
b={}
for i in range(len(a)):
    c=a[i]
    b[c]=b.get(c,0)+1
list=[]
for k,v in b.items():
    list.append([k,v])
list.sort(key=lambda x:x[1],reverse=True)
if list[1[1]]==list[2[1]]:
    print(list[1])
    print(list[2])
if list[1[1]]>list[2[1]]:
    print(list[1])
