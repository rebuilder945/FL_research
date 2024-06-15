l=list(input().split(' '))
dic={}
for i in l:
    dic[i]=l.count(i)
a=max(dic.values())
l2=[]
for i in dic:
    if dic[i]==a:
        l2.append(i)
l2.sort()
for i in l2:
    print("{} {}".format(i,a))
