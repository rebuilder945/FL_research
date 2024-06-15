a=list(input("").split(' '))
b=[(i,a.count(i)) for i in a]
s=[a.count(i) for i in a]
dic=dict(b)
for x in sorted(list(dic.keys())):
    if  dic[x]==max(s):
        print(x,max(s))
