dic1={}
lst=input().split()
for i in range(len(lst)):
    dic1[lst[i]]=lst.count(lst[i])
lis1=list(dic1.values())
lis1.sort(reverse=True)
n=lis1.count(lis1[0])
lis2=[]
for k,v in dic1.items():
    lis2.append([k,v])
for i in range(n):
    print(lis2[i][0],lis2[i][1])
