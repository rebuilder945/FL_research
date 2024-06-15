lst=list(input())
a,b,c,d,e=0,0,0,0,0
for x in lst:
    if x.isdigit():
        a+=1
    elif x.isupper():
        b+=1
    elif x.islower():
        c+=1
    else:
        d=d+1
if len(lst)>=8:
    e+=1
lst1=[a,b,c,d,e]
jishu=0
for i in lst1:
    if i!=0:
        jishu=jishu+1
print(jishu)
    

