lst=eval(input())
set1=''
str1=set1.join(lst)
str2=set(str1)
str2=list(str2)
str2.sort()
for i in str2:
    t=0
    for j in str1:
        if i in j:
            t+=1
s=','.join(i,t)
print(s)
