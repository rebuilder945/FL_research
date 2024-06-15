names=input().split (',')
scores=input().split(',')
k=[]
for i in range(len(names)):
    for x in range(len(scores)):
        if i==x:
           
            k.append([names[i],int(scores[x])])
k.sort(key=lambda x:x[1],reverse=False)
print(k)
            
