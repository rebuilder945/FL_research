item=list(input().split())
dic={}
for i in item:
    dic[i]=dic.get(i,0)+1
b=[] 
for k,v in dic.items():   
    b.append([k,v])          
    b.sort(key=lambda x:x[1],reverse=True)   
c=1
for i in range(0,len(b)-1):
    if b[i][1]==b[i+1][1]:
        c=c+1
for i in range(c):
    print(b[i][0], b[i][1])

