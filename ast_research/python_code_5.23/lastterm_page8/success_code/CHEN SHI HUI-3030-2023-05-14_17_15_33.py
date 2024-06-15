sums=list(input().split(','))
sums2=list(eval(input()))
sum4=[]
for i in range(len(sums)):
    sum3=[sums[i],sums2[i]]
    sum4.append(sum3)
sum4.sort()    
print(sum4)
    
