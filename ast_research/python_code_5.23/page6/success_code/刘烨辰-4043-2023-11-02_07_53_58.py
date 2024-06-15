a=eval(input())
b=''
c=[]
for x in a:
    b=b+x
for i in b:
    c.append(i)
for i in range(0,26):
    if c.count(chr(ord('a')+i))>0:
        print("%s,%d"%(chr(ord('a')+i),c.count(chr(ord('a')+i))))
