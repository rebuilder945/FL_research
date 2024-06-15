nums=eval(input())
a=max(nums)
b=min(nums)
n1=nums.count(a)
n2=nums.count(b)
p=0
q=0
while p<n1:
    nums.remove(a)
    p+=1
while q<n2:
    nums.remove(b)
    q+=1
if a==b:
    print("[]")
print(nums)
