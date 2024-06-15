lst=eval(input())
dic={}
for str in lst:
    for i in str:
        dic[i]=dic.get(i,0)+1
for i in sorted(dic.keys()):
    print("%s,%d"%(i,dic[i]))

