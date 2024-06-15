st=input()
lst=st.split(" ")
x,y=(int(i) for i in input().split())
t=lst[x]
lst[x]=lst[y]
lst[y]=t
print(lst)

