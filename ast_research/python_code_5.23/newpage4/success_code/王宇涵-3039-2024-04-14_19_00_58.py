lst1 = eval(input())
lst1 =list(lst1)
a = max(lst1)
b = min(lst1)
jishu1 = 0
jishu2 = 0
for x in lst1:
    if x==a or x==b:
       lst1[jishu2]='#'
       jishu1+=1
    jishu2+=1
    while jishu1>0:
       lst1.remove('#') 
       jishu1-=1
print(lst1)

