strls=input().split()
sum=[]
str=[]
for i in strls:
    sum.append(strls.count(i))
for i in strls:
    if strls.count(i)==max(sum) and i not in str:
        str.append(i)
        str.sort()
for x in str:
    print(x,max(sum))
