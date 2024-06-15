ls1=input().split(',')
ls2=input().split(',')
dic={}
for x in range(len(ls1)):
    dic[ls1[x]]=int(ls2[x])
score_ls=[]
for k,v in dic.items():
    score_ls.append([k,v])
score_ls.sort(key=lambda x:x[1])
print(score_ls)
