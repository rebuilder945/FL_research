lst=eval(input())
dic0={}
for x in lst:
    for y in x:
        dic0[y]=dic0.get(y,0)+1
for k,v in dic0.items():
    print('{},{}'.format(k,v))
