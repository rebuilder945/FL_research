ls = eval(input())

ls1 = []

st = ""

for i in ls:

    st+=i

for x in st:

    if x not in ls1:

        ls1.append(x)

        print("%s,%i"%(x,st.count(x)))
