lst=eval(input())
set1=''
str1=set1.join(lst)
str2=set(str1)
print(str2)
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
