M=eval(input())
count=[]
mcount=mnum=len(M)
while(mcount>0):
    if(M[mcount-1] not in count):
        count.append(M[mcount-1])
    mcount-=1
count.reverse()
print(count)
