s=input() or "#"
count=0
sum=0
while(s!="#"):
    sum+=int(s)
    count+=1
    s=input() or "#"
print(sum,count)
