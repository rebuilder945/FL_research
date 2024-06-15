num=eval(input())
numlist1=list(str(num))
numlist2=list(map(int,numlist1))
m=""
for i in numlist2:
    i=(i+5)%10
for x in range(len(numlist2)//2):
    numlist2[x]=numlist2[-x]
for a in range(len(numlist2)):
    b=str(numlist2[a])
    m+=b
print(int(m))
