a=eval(input())
lst1=[]
lst2=[]
for i in a:
    lst1.append(i[0])
    lst2.append(i[1])
dict={}
for i in range(len(lst1)):
    dict[lst1[i]]=lst2[i]
if 201800<a<201821:
    b=dict[a]
    print(b)
else:
    print("None")



