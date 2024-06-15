ls=eval(input())
str1=''.join(ls)
d=[]
for x in str1:
    c=str1.count(x)
    d.append([x,c])
d.sort(key=lambda x:x[0])
m=[]
for i in  d:
    if i not in m:
        m.append(i)
        print(i[0],i[1],sep=',')
    
