import sys
f=open('score.txt','r+')
g=open('sorted.txt','w+')
sys.stdout=g
c=[]
for line in f.readlines():
    a=list(line.split(','))
    b=eval(a[-1])+eval(a[-2])+eval(a[-3])
    c.append(b)
c.sort(reverse=True)
for line in list(f.readlines()):
    d=list(line.split(','))
    for i in c:
        if i==eval(d[-1])+eval(d[-2])+eval(d[-3]):
            d[0],d[1]=d[1],d[0]
            print(','.join(a))
            print('aaa')
f.close()
g.close()
        
