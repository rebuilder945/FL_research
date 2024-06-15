s=input() or "None"
count=0
sum=0
while(s!="None"):
    sum+=int(s)
    count+=1
    s=input() or "None"
print(sum,count)
