s=eval(input())
st=[]
for m in s:
    for n in m:
        st.append(n)
st.sort()
lst=[]
for x in st:
    if x not in lst:
        print(x,s.count(x))
        lst.append(x)
