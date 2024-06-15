ls=input().split(",")
for i in range(len(ls)):
    ls[i]=ls[i]+5
    ls[i]=ls[i]%10
for x in range(len(ls)//2):
    ls[i],ls[len(ls)-1-i]=ls[len(ls)-1-i],ls[i]
print(list(map(int,ls)))
