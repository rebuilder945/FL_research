dic={}
lst=[]
lst2=[]
s=input()
while s!="abc":
    dic[s]=dic.get(s,0)+1
    s=input()
for x in dic.keys():
    lst.append(x)
for y in dic.values():
    lst2.append(y)
lst3=[]
a=len(lst)
for z in range(a):
    lst3=lst3+[[lst[z],lst2[z]]]
b=max(lst2)
lst4=[]
for i in range(a):
    if lst3[i][1]==b:
        lst4.append(lst3[i])
print("%s %d"%(lst4[0][0],lst4[0][1]))




