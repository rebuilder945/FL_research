lst =eval(input())
lst.sort()
sum =''
for i in range(len(lst)):
    sum =sum+str(lst[i])
sum=sum.reverse()
print(int(sum))

    
