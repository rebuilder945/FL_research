str1=input()
names=[str(i) for i in str1.split(',')]
nums=eval(input())
x2=[]
shu=0
long=len(names)
while long>0:
    x1=[]
    x1.append(names[shu])
    x1.appeng(nums[shu])
    x2.appeng(x1)
    long-=1
    shu+=1
x3=sorted(x2,key=lambda x:x[1])
print(x3)
