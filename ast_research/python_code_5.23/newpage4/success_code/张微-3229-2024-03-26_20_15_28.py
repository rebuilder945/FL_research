nums = eval(input())
a=[]
c=[]
count=0
record=[0,0,0,0,0,0,0,0,0,0]
numrange=[0,1,2,3,4,5,6,7,8]
for numa in nums:
    for numb in numrange:
        if int(numa)-1 == int(numb):
            record[numb]=record[numb]+1
for i in range(9):
    if record[i]==1:
        a.append(i+1)
        count=count+1
c=sorted(a)
d=''.join(str(c))
if count==0:
    print("False")
else:
    print(d[1:-1])

