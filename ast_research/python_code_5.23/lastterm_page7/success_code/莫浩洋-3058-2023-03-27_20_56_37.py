a = 1
d={}
n = input()
while n!="q" :
    d[n]=d.get(n,0)+1
    n=input()
ls = list(d.items() )
ls.sort(key = lambda x:x[1],reverse=True)
print("{} {}".format(ls[0][0],ls[0][1]))
