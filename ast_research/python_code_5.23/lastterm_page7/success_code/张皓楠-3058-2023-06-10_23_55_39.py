dic={}
i=input()
while i!='q':
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
    i=input()
jishu=0
for i in dic.values():
    if i>jishu:
        jishu=i
for i in dic.keys():
    if dic[i]==jishu:
        print("{} {}".format(i,jishu))

