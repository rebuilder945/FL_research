lst1=[]
a=input()
while a!='q':
    lst1.append(a)
    a=input()

dic1={}
for i in lst1:
    dic1[i]=dic1.get(i,0)+1

lst2=[]
for k,v in dic1.items():
    lst2.append([k,v])

lst2.sort(key=lambda x:x[1],reverse=True)
print(lst2[0][0],lst2[0][1])
