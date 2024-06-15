dic={}
while True:
    s=input()
    if s =='q':
        break
    if s in dic:
        dic[s]+=1
    else:
        dic[s]=1
ls=[]
for x,y in dic.items():
    ls.append([x,y])
    ls.sort(key=lambda x:x[1],reverse=True)
print('%s %i'%(ls[0][0],ls[0][1]))
