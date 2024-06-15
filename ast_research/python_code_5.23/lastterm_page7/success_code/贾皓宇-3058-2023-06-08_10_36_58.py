lst=[]
while True:
    a=input()
    lst.append(a)
    if a=='q':
        break
dic={}
lst2=[]
for i in lst:
    d=lst.count(i)
    dic[d]=i
    lst2.append(d)
print(dic[max(lst2)],max(lst2))
