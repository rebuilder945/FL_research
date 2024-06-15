s=input() or 'q'
count={}
while s !='q':
    count[s]=count.get(s,0)+1
    s=input() or 'q'
countlist=list(count.items())
countlist.sort(key=lambda X: X[1],reverse=True)
b=countlist[0][0]
c=countlist[0][1]
print(b,c,sep=' ')
