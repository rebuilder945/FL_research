b={}
while True:
    a=input()
    if input()=="q":
        break
    b[a]=b.get(a,0)+1
lst=[]
for k,v in b.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[1],reverse=True)
c=lst[1][0]
d=lst[1][1]
print("{} {}".format(c,d))
