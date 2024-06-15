lst=[0,1,2,3,2]
lst.sort(reverse=True)
sum=''
for i in range(len(lst)):
    sum+=str(lst[i])
print(int(sum))
