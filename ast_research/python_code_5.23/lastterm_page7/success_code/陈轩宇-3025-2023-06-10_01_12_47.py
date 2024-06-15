a = input().split(" ")
dic1 = {}
for i in a:
    if i in dic1:
        dic1[i]+=1
    else:
        dic1[i]=1
jishu = 1
for i in dic1.values():
    if i>=jishu:
        jishu=i
        jishu = int(jishu)
for i in dic1.keys():
    if dic1[i]==jishu:
        print("{} {}".format(i,jishu))       
