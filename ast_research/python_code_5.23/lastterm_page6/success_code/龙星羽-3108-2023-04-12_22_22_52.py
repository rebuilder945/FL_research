ls=eval(input())
str={}
for str in ls:
    for s in str:
        str[s]=str.get(s,0)+1
for i in sorted(str.keys()):
    print('%s,%d'%(i,str[1]))
