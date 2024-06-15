a=["aaab", "cccdz"]
b=""
c={}
for i in a:
    b+=i
for i in b:
    c[i]=c.get(i,0)+1
print(c)
lst=[]
for k,v in c.items():
    lst.append([k,v])
lst.sort(key=lambda x:x[0],reverse=False)
print(lst)
for i in lst:

        print("{},{}".format(i[0],i[1]))


