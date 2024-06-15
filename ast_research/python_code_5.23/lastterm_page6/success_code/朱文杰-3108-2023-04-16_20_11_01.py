lst=eval(input())
set=''
str1=set.join(lst)
str2=set(str1)
str2=list(str2)
str2.sort()
s=0
for i in str2:
    t=0
    s=s+1
    for j in str1:
        if i in j:
            t+=1
    print(i,t)
