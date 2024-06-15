a=eval(input())
b=''
for i in a:
    b+=i
c=[chr(x) for x in range(97,123)]
d=""
for i in c:
    d+=i
for x in d:
    e=b.count(x)
    if b.count(x)!=0:
        print("%s,%.d"%(x,e))

    
