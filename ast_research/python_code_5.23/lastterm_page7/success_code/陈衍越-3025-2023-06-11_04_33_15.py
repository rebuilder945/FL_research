dct={}
a=input().split()
for i in a:
    if i not in dct:
        dct[i]=1
    else:
        dct[i]+=1
jishu=0
for i in dct.values():
    if i>jishu:
        jishu=i
zf=[]
j=0
for x in dct.keys():
    if dct[x]==jishu:
        zf.append(x)
        print(zf[j],jishu)
        j+=1

        

