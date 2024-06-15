M=eval(input())
count=[]
mcount=mnum=len(M)
while(mcount>0):
    if(M[mcount] not in count):
        count.append(M[mcount])
    mcount-=1
count.reverse()
print(count)
