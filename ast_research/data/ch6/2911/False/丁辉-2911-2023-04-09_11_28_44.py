num=eval(input())
numlist1=list(str(num))
numlist2=list(map(int,numlist1))
for i in numlist2:
    i=(i+5)%10
# for x in range(len(numlist2)//2):
#     numlist2[x]=numlist2[-(x+1)]
m="".join(map(str,numlist2))
print(int(m))
