lst = eval(input())
s = []
s1=[]
for x in lst:
    for i in x:
        s.append(i)
        if i not in s1:
            s1.append(i)
s1.sort()
for i in s1:
    n=s.count(i)
    print("%s,%d"%(i,n))
            
            
