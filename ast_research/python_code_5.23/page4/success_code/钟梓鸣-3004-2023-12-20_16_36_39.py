nums=eval(input())
a=[]
nums.sort()
for num in nums:
    i=2
    flag=1
    if(num!=1 and num!=0):
        while(i<num):
            if(num%i==0):
                flag=0
            i+=1
        if(flag):
            a.append(num)
print(a)
