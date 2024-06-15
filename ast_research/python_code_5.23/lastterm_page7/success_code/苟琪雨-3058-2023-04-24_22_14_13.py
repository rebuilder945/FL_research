dic1={}
lst=[]
while True:
    n=input()
    if n=='q':
        break
    lst.append(n)
for i in range(len(lst)):
    dic1[lst[i]]=lst.count(lst[i])
lis1=[]
for k,v in dic1.items():
    lis1.append([k,v])
lis1.sort(key=lambda x:x[1],reverse=True)
print(lis1[0][0],lis1[0][1])
