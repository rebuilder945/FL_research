a=eval(input())
av=0
c=0
for x in a:
    c=c+x
    av=av+1
    ave=c/av
    b=ave-int(ave)
if b==0:
    print(int(ave))
elif b!=0:
    print("*2f"%ave)
