s=input().split()
dic={}
ls=[]
for i in s:
    dic[i]=dic.get(i,0)+1
for k,v in dic.items():
    ls.append([k,int(v)])
ls.sort(key=lambda x:(-x[1],x[0]))
count=1
for i in range(len(ls)-1):
    if ls[i][1]==ls[i+1][1]:
        count+=1
for i in range(count):
    print(ls[i][0],ls[i][1],end="")
    print()



