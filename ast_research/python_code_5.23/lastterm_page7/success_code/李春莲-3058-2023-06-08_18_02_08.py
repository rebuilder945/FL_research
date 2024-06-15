dic={}
a=input()
while a!='q':
    if a in dic:
        dic[a]+=1
    else:
        dic[a]=1
    a=input()
t=0
for a in dic.values():
    if a>t:
        t=a
for a in dic.keys():
    if dic[a]==t:
        print("{} {}".format(a,t))
