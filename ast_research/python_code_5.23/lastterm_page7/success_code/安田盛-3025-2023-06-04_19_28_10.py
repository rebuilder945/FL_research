s=input().split()
dic={}
for i in s:
    dic[i]=dic.get(i,0)+1
lst=[]
for x,y in dic.items():
    lst.append([x,y])
lst.sort(key=lambda x:x[1])
lst1=[]
x=lst[-1][1]
for i in range(len(lst)):
    if lst[i][1]==x:
        lst1.append(lst[i])
lst1.sort(key=lambda x:x[0])
for i in range(len(lst1)):
    print("%s %d"%(lst1[i][0],lst1[i][1]))




            




