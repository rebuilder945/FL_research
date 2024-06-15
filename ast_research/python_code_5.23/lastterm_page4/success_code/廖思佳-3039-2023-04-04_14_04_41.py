nums=eval(input())
a=max(nums)
b=min(nums)
m=0 #记录最大值的个数
n=0 #记录最小值的个数
for i in range(len(nums)):
     if a==nums[i] :
        m+=1
     if b!=a and b==nums[i] :
         n+=1
        
              

num=list(nums)
for x in range(m) :
    num.remove(a)

for  y  in range (n) :
    num.remove(b)


print(num)    

               

