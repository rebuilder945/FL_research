ls=eval(input())
lst=[]
m=0
for i in ls:
    if ls.count(i)==1:
       lst.append(i)
    else: 
        m+=1
if m==len(ls):
    print("False")
else:
    lst.sort()
    if len(lst)==1:
        a=lst[0]
        print(a)
    else:
        lst1=str(lst)
        lst2=lst1.strip("[]")
        lst3=lst2.replace(" ","")
        print(lst3)



