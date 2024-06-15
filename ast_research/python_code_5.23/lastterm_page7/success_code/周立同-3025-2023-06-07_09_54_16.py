lst=input().split()
dic={}
a=0
lst2=[]
for i in lst:
    dic[i]=dic.get(i,0)+1
    if dic[i]>a:
        a=dic[i]
lst3=list(dic.keys())
lst3.sort()
for b in lst3:
    if dic[b]==a:
       print(b,a)
