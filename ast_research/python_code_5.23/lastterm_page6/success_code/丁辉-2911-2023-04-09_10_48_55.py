num=eval(input())
numlist=list(num)
for i in numlist:
    i=(i+5)%10
for x in range(len(numlist)//2):
    numlist[len(x)]=numlist[-len(x)]
print(int(numlist))
