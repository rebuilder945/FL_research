s=input().split()
dic={}
for x in s :
    dic[x]=dic.get(x,0)+1
st=[]
for k,v in dic.items():
    st.append([k,v])
st.sort(key=lambda x:x[1],reverse=True)
i=0
n=len(st)
while True:
    if i+1==n:
        i+=1
        break
    if st[i][1]==st[i+1][1]:
        i+=1
    else:
        i+=1
        break
st1=sorted(st[0:i])
for x in range(i):
    for y in st1[x]:
        print(y,end=' ')
    print('')
