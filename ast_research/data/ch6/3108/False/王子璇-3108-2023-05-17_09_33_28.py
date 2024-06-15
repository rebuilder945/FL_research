s=eval(input())
st=[]
for m in s:
    for n in m:
        st.append(n)
st.sort()
lst=[]
for x in n:
    for y in x:
        if y not in lst:
            print(y,s.count(y))
            lst.append(y)



