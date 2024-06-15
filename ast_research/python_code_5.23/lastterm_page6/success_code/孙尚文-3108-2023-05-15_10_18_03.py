strlist=eval(input())
dict={}
for str in strlist:
    for i in str:
        dict[i]=dict.get(i,0)+1
for i in sorted(dict.keys()):
    print("%s,%d"%(i,dict[i]))
