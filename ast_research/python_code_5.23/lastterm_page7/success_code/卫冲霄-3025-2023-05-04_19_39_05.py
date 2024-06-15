s=input().split()
ls={}
ls1=[]
for i in s:
    ls[i]=ls.get(i,0)+1
for k,v in ls.items():
    ls1.append([k,v])
ls1.sort(key=lambda x:x[1],reverse=True)
a=1
for i in range(len(ls1)):
    if ls1[i][1]==ls1[i+1][1]:
        a+=1
    else:
        break
for i in range(a):
    print(*(ls1[i]))

