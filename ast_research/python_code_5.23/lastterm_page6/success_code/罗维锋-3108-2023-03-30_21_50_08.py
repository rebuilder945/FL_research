s=eval(input())
m="".join(s)
for i in list(map(chr,range(97,123))):
    x=m.count(i)
    if m!=0:
        print(i,x)
