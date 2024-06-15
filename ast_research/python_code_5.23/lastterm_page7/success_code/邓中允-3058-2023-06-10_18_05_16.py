n=input()
d={}
while n!='q':
    d[n]=d.get(n,0)+1
    n=input()
a=0
for i in d.values():
    if i>a:
        i=a
for i in d.keys():
    if d[i]==a:
        print("{} {}".format(i,a))

