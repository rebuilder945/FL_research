from tkinter import ANCHOR


s=input() or "q"
st={}
while s!="q":
    if s in st.keys():
        st[s]+=1
    else:
        st[s]=1
    s=input() or "q"
stlist=list(st.items())
stlist.sort(key=lambda x:x[1],reverse=True)
print(stlist[0][0],stlist[0][1])
