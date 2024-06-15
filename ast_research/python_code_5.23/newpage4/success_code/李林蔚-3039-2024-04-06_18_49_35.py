a=eval(input())
b=max(a)
c=min(a)
jishu1=0
jishu2=0
for x in a:
    if x==b or x==c:
        a[jishu2]='#'
        jishu1+=1
    jishu2+=1
while jishu1>0:
    a.remove('#')
    jishu1-=1
print(a)
