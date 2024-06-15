lst=eval(input())
lst2=[]
for iv in lst:
    for xv in range(len(iv)):
        lst2.append(iv[xv])
for zv in ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']:
    time=lst2.count(zv)
    if time >=1:
        print("%s,%.d"%(zv,time))

