a=eval(input())
b=""
for x in a:
    b+=x
m=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
for x in m:
    if x in b:
        print("%s,%d"%(x,b.count(x)))
