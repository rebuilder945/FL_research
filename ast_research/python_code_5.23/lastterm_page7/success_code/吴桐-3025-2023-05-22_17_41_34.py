s=input()
li=list(s.split())
st={}
for i in li:
    st[i]=li.count(i)
ls=[]
for k,v in st.items():
    ls.append([k,v])
ls.sort(key=lambda x:x[1],reverse=True)
a=1
for i in range(len(ls)-1):
    if ls[i][1]==ls[i+1][1]:
        a+=1
for i in range(a):
    print(ls[i][0],ls[i][1])

