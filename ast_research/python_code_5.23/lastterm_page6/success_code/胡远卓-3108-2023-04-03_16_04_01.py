x=eval(input())
for i in range(0,26):
    res=0
    for j in range(len(x)):
        res+=x[j].count(chr(ord('a')+i))
    if res>0:
        print("%c,%d"%(chr(ord('a')+i),res))
