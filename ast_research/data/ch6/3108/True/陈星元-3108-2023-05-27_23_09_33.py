str=eval(input())
dict={}
for i in str:
    for x in i:
        dict[x]=dict.get(x,0)+1
ls=[]
for k,v in dict.items():
    ls.append([k,v])
ls.sort(key=lambda x:ord(x[0]))
for x in ls:
    print("{},{}".format(x[0],x[1]))


