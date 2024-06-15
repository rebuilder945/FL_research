item=input()or"q"
dic={}
while item!='q':
    dic[item]=dic.get(item,0)+1
    item=input()or"q"
a=0
for i in dic:
    if dic[i]>a:
        a=dic[i]
for i in dic:
    if dic[i]==a:
        print(i,a)
