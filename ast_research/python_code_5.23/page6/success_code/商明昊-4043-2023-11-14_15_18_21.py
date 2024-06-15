t = input()
t=t.replace("[","").replace("]","").replace('"','').replace(',','').replace(' ','')
#t=t.split(',')
#t = list(t)
ls = []
for i in t:
    if i not in ls:
        ls.append(i)
for x in ls:
    n =t.count(x)
    print("%s,%d"%(x,n))
