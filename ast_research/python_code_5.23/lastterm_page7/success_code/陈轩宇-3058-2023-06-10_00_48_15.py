item = input()
dic1 = {}
while (item!="q"):
    if item in dic1:
        dic1[item]+=1
    else:
        dic1[item]=1
    item = input()
jishu=0
for i in item.value():
    if i > jishu:
        jishu = i
for i in item.keys():
    if item[i]==jishu:
        print("{} {}".format(i,jishu))        

