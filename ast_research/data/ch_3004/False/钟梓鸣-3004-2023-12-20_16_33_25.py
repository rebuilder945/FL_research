nums=eval(input())
a=[]
for num in nums:
    i=2
    flag=1
    while(i<num):
        if(num%i==0):
            flag=0
        i+=1
    if(flag):
        a.append(num)
print(a)
