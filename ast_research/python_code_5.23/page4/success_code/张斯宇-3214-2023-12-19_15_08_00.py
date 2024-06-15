lst=eval(input())

count=0
for i in lst:
    if i==0: count+=1


ans=[i for i in lst if i!=0]+[0]*count
print(ans)
